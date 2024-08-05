from django.http import Http404, JsonResponse 
from django.shortcuts import render
# import models
from .models import Quest,Movie,Reservation
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from .serializers import QuestSerializers , MovieSerializers,ReservationSerializers
from rest_framework.views import APIView
from rest_framework import generics,mixins , viewsets ,filters


# Create your views here.
# 11  this method with out rest framwork and no query this fbv 

def first_method(req):

    quest =[
        {'id':1,
         'name':'ali',
         },
         {
             'id': 2,
             "name":'boss'
         }
    ]
   
    for i in range (10):
        quest.append({
             'id': i,
             "name":'new' + str(i) 
         })
    return JsonResponse (quest, safe=False)

# 2 second method no rest from model db

def second_method(req):
    data = Quest.objects.all()

    response =list(data.values('name','mobile'))
    # response =list(data.values())

    return JsonResponse(response ,safe=False)



 
# third method is a rest frame django

@api_view(['GET','POST'])
def fbv_list(req):
    # this get
    if req.method == 'GET':
        quests = Quest.objects.all()
        serializer = QuestSerializers(quests,many=True)
        return Response(serializer.data)
    # this post 
    elif req.method == 'POST':
        serializer = QuestSerializers(data= req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def fbv_pk(req,pk):

    try:
        guest = Quest.objects.get(pk=pk)
    except Quest.DoesNotExist :
        return Response( status.HTTP_404_NOT_FOUND)    
    # this GET
    if req.method == 'GET':
        serializer = QuestSerializers(guest)
        return Response(serializer.data)

    # PUT  or UPDATE
    elif req.method == 'PUT':
        serializer = QuestSerializers(guest,data= req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    # DELETE
    if req.method == 'DELETE':
        guest.delete()
        return Response(status.HTTP_208_ALREADY_REPORTED)
    

#  method 4 cbv class besed view
class CbvList(APIView):
    def get(self,r):
            guest = Quest.objects.all()
            serializer = QuestSerializers(guest,many=True)
            return Response(serializer.data)
    def post(self,r):
        print(r.data)
        serializer = QuestSerializers(data=r.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


# edit data py cbv with pk

class CbvPk(APIView):
    def get_object(self,pk):
        try:
           return Quest.objects.get(pk=pk)
        except Quest.DoesNotExist:
            raise Http404

    def get(self,r,pk):
        guest = self.get_object(pk)
        serializer = QuestSerializers(guest)
        return Response(serializer.data)  
    def put(self,r,pk):
        guest = self.get_object(pk)
        serializer = QuestSerializers(guest,data=r.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    
    def delete(self,r,pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_208_ALREADY_REPORTED)
        

# 5 method no. 5 mixins and  generics beter form
class mixin_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    # the var must be the same name
    queryset = Quest.objects.all()
    serializer_class = QuestSerializers
    def get(self,req):
        return self.list(req)
    def post(self,req):
        return self.create(req)

# mixins with pk
class mixin_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializers
    def get(self,req,pk):
        return self.retrieve(req)
    def put(self,req,pk):
        return self.update(req)
    def delete(self,req,pk):
        return self.destroy(req)



# 6 generics method 
class generics_list(generics.ListCreateAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializers    

# 6.1 generic with pk edite delete 
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializers


# 7 view set views
class viewsets_guest(viewsets.ModelViewSet):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializers

# now get data from all models in db

class viewset_move(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['movie_name']

class viewset_res(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers    

# find movi this used only in postman
@api_view(['GET'])
def findmovie(request):
    # print(request.data)
    movies = Movie.objects.filter(
        # hall = request.data['hall'],
        movie_name = request.data['name'])
    serializer = MovieSerializers(movies, many= True)
    return Response(serializer.data)

# now make new resrvation 

@api_view(['POST'])
def new_res(req):
    movie = Movie.objects.get(movie_name = req.data['mname'])

    customer = Quest()
    customer.name = req.data['cname']
    customer.mobile = req.data['mobile']
    customer.save()
    
    res = Reservation()
    res.quest = customer
    res.movie = movie
    res.save()
    return Response(status.HTTP_201_CREATED)


