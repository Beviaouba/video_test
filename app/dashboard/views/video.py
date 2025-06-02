from django.views.generic import View
from django.shortcuts import redirect,reverse

from app.libs.base_render import render_to_response
from app.utils.permission import dashboard_auth
from app.model.video import VideoType,FromType,NationalityType,Video,VideoSub,IdentityType,VideoStar
from app.utils.common import check_and_get_video_type

class ExternalVideo(View):
    TEMPLATE = 'dashboard/video/external_video.html'
    @dashboard_auth
    def get(self, request):
        error = request.GET.get('error','')
        data = {'error':error}

        videos = Video.objects.exclude(from_to = FromType.custom.value)
        data['videos'] = videos

        return render_to_response(request,self.TEMPLATE,data)

    def post(self,request):
        name = request.POST.get('name')
        image = request.POST.get('image')
        video_type = request.POST.get('video_type')
        from_to = request.POST.get('from_to')
        nation = request.POST.get('nation')
        info = request.POST.get('info')

        if not all([name,image,video_type,from_to,nation,info]):
            return redirect('{}?error={}'.format(reverse('external_video'),'缺少必要字段'))

        result = check_and_get_video_type(VideoType,video_type,'非法视频类型')
        if result.get('code') != 0:
            return redirect('{}?error={}'.format(reverse('external_video'),result['msg']))

        result = check_and_get_video_type(FromType,from_to,'非法来源')
        if result.get('code') != 0:
            return redirect('{}?error={}'.format(reverse('external_video'),result['msg']))

        result = check_and_get_video_type(NationalityType, nation, '非法国籍')
        if result.get('code') != 0:
            return redirect('{}?error={}'.format(reverse('external_video'), result['msg']))

        Video.objects.create(
            name=name,
            image=image,
            video_type=video_type,
            from_to=from_to,
            nationality=nation,
            info=info,
        )
        return redirect(reverse('external_video'))

class VideoSubView(View):
    TEMPLATE = 'dashboard/video/video_sub.html'

    @dashboard_auth
    def get(self, request,video_id):
        data = {}
        video = Video.objects.get(id=video_id)
        error = request.GET.get('error','')

        data['error'] = error
        data['video'] = video
        return render_to_response(request,self.TEMPLATE,data=data)

    def post(self,request,video_id):
        url = request.POST.get('url')

        video = Video.objects.get(pk=video_id)
        length_v = video.video_sub.count()
        try:
            VideoSub.objects.create(
                video=video,
                url=url,
                number=length_v + 1,
            )
        except:
            return redirect('{}?error={}'.format(reverse('video_sub',kwargs={'video_id':video_id}),'创建失败'))

        return redirect(reverse('video_sub',kwargs={'video_id':video_id}))

class VideoStarView(View):
    def post(self,request):
        name = request.POST.get('name')
        i = request.POST.get('i')
        video_id = request.POST.get('video_id')

        if not all([name,i,video_id]):
            return redirect('{}?error={}'.format(reverse('video_sub',kwargs={'video_id':video_id}),'缺少必要字段'))
        result = check_and_get_video_type(IdentityType,i,'非法身份')

        if result.get('code') != 0:
            return redirect('{}?error={}'.format(reverse('video_sub',kwargs={'video_id':video_id}),result['msg']))

        video = Video.objects.get(pk=video_id)
        try:
            VideoStar.objects.create(
                video=video,
                name=name,
                identity=i,
            )
        except:
            return redirect('{}?error={}'.format(reverse('video_sub',kwargs={'video_id':video_id}),'创建失败'))


        return redirect(reverse('video_sub',kwargs={'video_id':video_id}))

class StarDelete(View):

    def get(self,request,star_id,video_id):

        VideoStar.objects.filter(id=star_id).delete()

        return redirect(reverse('video_sub',kwargs={'video_id':video_id}))












