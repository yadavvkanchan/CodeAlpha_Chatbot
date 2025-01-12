# chatbot/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # If using csrf_exempt for testing
import json
from .chatbot import get_response

@csrf_exempt  # Temporary: You can remove this after making sure CSRF is correctly set up
def index(request):
    if request.method == 'POST':
        # Read JSON data from the request body
        try:
            data = json.loads(request.body)
            user_input = data.get('user_input', '').strip()  # Get user input from JSON
        except json.JSONDecodeError:
            return JsonResponse({'response': 'Invalid JSON format.'})

        # Debugging: print the received user input
        print(f"User Input: {user_input}")

        if user_input:  # Ensure input is not empty
            bot_response = get_response(user_input)  # Get chatbot's response
            print(f"Bot Response: {bot_response}")  # Debugging
            return JsonResponse({'response': bot_response})
        else:
            return JsonResponse({'response': 'Please enter a message.'})
    
    return render(request, 'chatbot/index.html')
