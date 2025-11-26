from django.shortcuts import render

# Create your views here.


# index dark
def index(request):
    # Create a context dictionary with the user groups
    context = {
        'user': None
    }
    return render(request, 'index.html', context)


def faqs(request):
    # Create a context dictionary with the user groups
    context = {
        'user': None
    }
    return render(request, 'faq.html', context)


def about_us(request):
    # Create a context dictionary with the user groups
    context = {
        'user': None
    }
    return render(request, 'about_us.html', context)


def legal(request):
    # Create a context dictionary with the user groups
    context = {
        'user': None
    }
    return render(request, 'legal.html', context)

def refer_and_earn(request):
    # Create a context dictionary with the user groups
    context = {
        'user': None
    }
    return render(request, 'refer_and_earn.html', context)

def contact_us(request):
    # Create a context dictionary with the user groups
    context = {
        'user': None
    }
    return render(request, 'contact_us.html', context)


# views.py
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def contact_form_submit(request):
    try:
        # Get form data
        data = request.POST
        print("=== Contact Form Submission ===")
        print(f"Received data: {data}")

        # Honeypot validation
        honeypot = data.get('website', '').strip()
        if honeypot:  # If honeypot field is filled, it's a bot
            print("Bot detected via honeypot")
            return JsonResponse({
                'success': True,
                'message': 'Thank you for your message!'
            })

        # Extract form fields
        name = data.get('form_name', '').strip()
        subject = data.get('form_subject', '').strip()
        email = data.get('form_email', '').strip()
        message = data.get('form_message', '').strip()

        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")

        # Validate required fields
        if not all([name, subject, email, message]):
            print("Validation failed: missing fields")
            return JsonResponse({
                'success': False,
                'message': 'All fields are required.'
            })

        # Email content
        email_subject = f"New Contact Form: {subject}"
        email_body = f"""
            New contact form submission:

            Name: {name}
            Email: {email}
            Subject: {subject}

            Message:
            {message}

            ---
            This email was sent from your website contact form.
                    """

        # Create email
        email_msg = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email='no-reply@gemscend.com',  # Replace with your email
            to=['no-reply@gemscend.com'],           # Replace with your receiving email
            cc=[email],
            reply_to=[email],
        )

        # Print EmailMessage details
        print("=== EmailMessage Details ===")
        print(f"From: {email_msg.from_email}")
        print(f"To: {email_msg.to}")
        print(f"CC: {email_msg.cc}")
        print(f"Reply-To: {email_msg.reply_to}")
        print(f"Subject: {email_msg.subject}")
        print("=============================")

        # Send email
        print("Sending email...")
        email_msg.send(fail_silently=False)
        print("Email sent successfully!")
        print(f"Email details: {email_msg}")

        return JsonResponse({
            'success': True,
            'message': 'Thank you for your message! We will get back to you soon.'
        })

    except Exception as e:
        print(f"Email error: {e}")
        import traceback
        traceback.print_exc()  # Print full error stack
        return JsonResponse({
            'success': False,
            'message': 'An error occurred. Please try again later.'
        })
