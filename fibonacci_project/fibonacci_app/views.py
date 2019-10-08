from django.shortcuts import render
from fibonacci_app.models import Fibonacci
from django.views import View
import time


def get_nth_fibonacci(input):
    """
        Returns fobonacci number for given count
    """
    if input < 2:
        return 1

    else:
        first_fib = 1
        second_fib = 1

        for numeric in range(2, input):
            sum = first_fib + second_fib
            first_fib = second_fib
            second_fib = sum

        return second_fib


class FibonacciView(View):
    def get(self, request):
        input = request.GET.get('input')
        if input is None:
	        return render(request, 'index.html')
        else:
            start_time = time.time()
            input = int(input)
            output = get_nth_fibonacci(input)
            end_time = time.time() - start_time
            duration = str(end_time)[0:3]
            query = Fibonacci.objects.create(
	            					input=input,
	            					output=output,
	            					duration=duration
	            				)
            query.save()
            data = {'input': input,
                    'output':output,
                    'duration':duration}

        return render(request, 'index.html', data)
