from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


from send.forms import EmailForm


def send_message(request):

    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            message = cd['message']
            from_send = cd['send_from']
            recipient = cd['recipient']
            # send the email to the recipent
            try:
                send_mail(subject, message, from_send, (recipient,))

                # set the variable initially created to True
                messageSent = True
            except Exception as e:
                type_send = type(from_send)
                return HttpResponse(
                    f'Error - {e}, fields - {type_send} is {from_send},'
                    f'{recipient}'
                )

    else:
        form = EmailForm()

    return render(
        request,
        'index.html',
        {
            'form': form,
            'messageSent': messageSent,
        }
    )
