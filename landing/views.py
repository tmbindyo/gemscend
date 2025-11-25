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
import json

@csrf_exempt
@require_POST
def contact_form_submit(request):
    try:
        # Get form data
        data = request.POST

        print(f"data:{data}")
        
        name = data.get('form_name', '').strip()
        subject = data.get('form_subject', '').strip()
        email = data.get('form_email', '').strip()
        message = data.get('form_message', '').strip()
        
        # Validate required fields
        if not all([name, subject, email, message]):
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
            from_email='noreply@yourdomain.com',  # Change this
            to=['recipient@company.com'],  # Main recipient
            cc=[email],  # CC the person who filled the form
            # Or use bcc instead of cc:
            # bcc=[email],
            reply_to=[email],  # So replies go to the submitter
        )
        
        # Send email
        email_msg.send(fail_silently=False)
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you for your message! We will get back to you soon.'
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'An error occurred. Please try again later.'
        })