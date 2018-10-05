from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from posts.models import Stat	

# Create your views here.
@csrf_exempt 
def index(request):
	

	if request.method == 'POST':

		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)

		st =Stat()
		st.headNum=body['headNum']
		st.paraNum=body['paraNum']
		st.save()

		return JsonResponse({'message':'added to DB'})

	if request.method =='GET':
		res={}
		finalStat= Stat()

		for p in Stat.objects.raw('SELECT * FROM posts_stat'):
			finalStat=p


		#query from sql
		res['headNum']=finalStat.headNum
		res['paraNum']=finalStat.paraNum
		return JsonResponse(res)
