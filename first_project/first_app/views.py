from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Calculation
from .serializers import CalculationSerializer
# Frontend view
def index(request):
    return render(request, "first_app/index.html")

# API views
class CalculationListCreateView(generics.ListCreateAPIView):
    queryset = Calculation.objects.all().order_by('-id')
    serializer_class = CalculationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        operand1 = float(data.get("operand1", 0))
        operand2 = float(data.get("operand2", 0))
        operator = data.get("operator", "+")
        try:
            if operator == "+":
                result = operand1 + operand2
            elif operator == "-":
                result = operand1 - operand2
            elif operator == "*":
                result = operand1 * operand2
            elif operator == "/":
                result = operand1 / operand2
            else:
                return Response({"error": "Invalid operator"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        calculation = Calculation.objects.create(
            operand1=operand1, operand2=operand2, operator=operator, result=result
        )
        serializer = self.get_serializer(calculation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CalculationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer

