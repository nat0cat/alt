from django.shortcuts import render
from .db_functions import * 
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Users, Assessments, UserStats, Questions, Responses
from .serializers import UserSerializer, AssessmentsSerializer, UserStatsSerializer, QuestionsSerializer, ResponsesSerializer
from .AnalyzeUserInput import * 

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    
class AssessmentsViewSet(viewsets.ModelViewSet):
    queryset = Assessments.objects.all()
    serializer_class = AssessmentsSerializer

    # def create(self, request, *args, **kwargs):
    #     # When send a post reqest, will send a link to the questions, and upate user stats 
    #     choice = request.data.get('choice')
    #     # You can now use the 'choice' value as needed

    #     # serializer = self.get_serializer(data=request.data)
    #     # serializer.is_valid(raise_exception=True)
    #     # self.perform_create(serializer)
    #     # return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     questions_url = 'http://127.0.0.1:8000/questions/{}/'.format(choice)

    #     response_data = {
    #         'Answer the questions': questions_url
    #     }

    #     return Response(response_data, status=status.HTTP_201_CREATED)

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    # def list(self, request, int_number=None):
    #     # returns list of questions for the selected assignments 
    #     queryset = Questions.objects.filter(question_id=int_number)
    #     serializer = QuestionsSerializer(queryset, many=True)
    #     return Response(serializer.data)

class UserStatsViewSet(viewsets.ModelViewSet):
    queryset = UserStats.objects.all()
    serializer_class = UserStatsSerializer

    # 


class ResponsesViewSet(viewsets.ModelViewSet):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializer

    # def update_userstats(user_id, assessment_id, count):
    #     user_instance = Users.objects.get(pk=user_id)
    #     userstat_exists = UserStats.objects.filter(user_id=user_id, assessment_id=assessment_id).exists()
    #     if userstat_exists:
    #         # update the userstat 

    def create(self, request, question_id, *args, **kwargs):
        user_id = request.data.get('user_id')
        response = request.data.get('response')

        # convert free text into num 
        int_choice = AnalyzeUserInput(response)

        # Call the insert_responses function
        # success = insert_responses(user_id, int_number, int_choice, None)
        
        user_instance = Users.objects.get(pk=user_id)
        question_instance = Questions.objects.get(pk=question_id)
        assessment_id = question_instance.assessment.assessment_id

        total_question = question_instance.assessment.num_questions

        if not success_userstats: 
            return Response({"errror": "ddddd"}, status=status.HTTP_400_BAD_REQUEST)

        response_exists = Responses.objects.filter(question_id=question_id, user_id=user_id).exists()
        if response_exists: 
            count = Responses.objects.filter(question_id=question_id, user_id=user_id).last().count 
        else:
            count = 0 

        # update the userstats model when all the questions are answered 
        success_userstats = update_userstats(user_id, assessment_id)

        try:
            response_instance = Responses.objects.create(
                user=user_instance,
                question=question_instance,
                num=int_choice,
                count=count + 1 
            )
            serializer = self.get_serializer(response_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


        if success and success_userstats:
            return Response({"message": "Response inserted successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Failed to insert response."}, status=status.HTTP_400_BAD_REQUEST)



