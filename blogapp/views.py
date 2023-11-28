# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from .models import NewsPost
#django.views.genericからLsitView、DatailViewをインポート
from django.views.generic import FormView
#django.views.genericからCreateViewをインポート
from django.views.generic import CreateView
#django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
#formsモジュールからNewsPostFormをインポート
from .forms import NewsPostForm
#formsモジュールからContactFormをインポート
from .forms import ContactForm
#django.contribからmessagesをインポート
from django.contrib import messages
#django.core.mailモジュールからEmailMessageをインポート
from django.core.mail import EmailMessage
#django.db.modelsからQオブジェクトをインポート
from django.db.models import Q

class IndexView(ListView):
    #index.htmlをレンダリング
    template_name = 'index.html'
    #object_listキーの別名を設定
    context_object_name = 'orderby_records'
    #モデルNewsPostのオブジェクトにorder_by()を適用して
    #NewsPostのレコードを投稿日時の降順で並べ替える
    queryset = NewsPost.objects.order_by('-posted_at')
    #1ページに表示するレコードの件数を設定
    paginate_by = 5

    #一致したタイトルの検索結果を表示する
    def get_queryset(self):
        queryset = NewsPost.objects.order_by('-posted_at')
        query = self.request.GET.get('q')
        if query:
            queryset = NewsPost.objects.order_by('-posted_at')
            queryset = queryset.filter(
            Q(title__icontains=query)
            )
        #indexで、「」を含む検索結果を表示させる
        messages.add_message(self.request, messages.INFO, query)
        return queryset

class CreateNewsView(CreateView):
    #forms.pyのNewsPostFormをフォームクラスとして登録
    form_class = NewsPostForm
    #レンダリングするテンプレート
    template_name = "post_news.html"
    #フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('blogapp:post_done')

    def form_valid(self, form):
        #commit=FalseしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # #投稿ユーザのidを取得してモデルのuserフィールドに格納
        # postdata.user = self.request.user
        #投稿データをデータベースに登録
        postdata.save()
        #戻り値はスーパークラスのform_vaild()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = 'post_success.html'

class NewsDetail(DetailView):
    #post.htmlをレンダリングする
    template_name = 'post.html'
    #クラス変数modelにモデルNewsPostを設定
    model = NewsPost

class DomesticView(ListView):
    #domestic_list.htmlをレンダリングする
    template_name = 'domestic_list.html'
    #クラス変数modelにモデルNewspostを設定
    model = NewsPost
    #object_listキーの別名を設定
    context_object_name = 'domestic_records'
    #category='domestic'のレコードを抽出して投稿日時の降順で並べ替える
    queryset = NewsPost.objects.filter(
        category='domestic').order_by('-posted_at')
    #1ページに表示するレコードの件数
    paginate_by = 5

class IntlView(ListView):
    #intl_list.htmlをレンダリングする
    template_name = 'intl_list.html'
    #クラス変数modelにモデルNewspostを設定
    model = NewsPost
    #object_listキーの別名を設定
    context_object_name = 'intl_records'
    #category='intl'のレコードを抽出して投稿日時の降順で並べ替える
    queryset = NewsPost.objects.filter(
        category='intl').order_by('-posted_at')
    #1ページに表示するレコードの件数
    paginate_by = 5

class PoliticsView(ListView):
    #politics_list.htmlをレンダリングする
    template_name = 'politics_list.html'
    #クラス変数modelにモデルNewspostを設定
    model = NewsPost
    #object_listキーの別名を設定
    context_object_name = 'politics_records'
    #category='politics'のレコードを抽出して投稿日時の降順で並べ替える
    queryset = NewsPost.objects.filter(
        category='politics').order_by('-posted_at')
    #1ページに表示するレコードの件数
    paginate_by = 5

class EconomyView(ListView):
    #economy_list.htmlをレンダリングする
    template_name = 'economy_list.html'
    #クラス変数modelにモデルNewspostを設定
    model = NewsPost
    #object_listキーの別名を設定
    context_object_name = 'economy_records'
    #category='economy'のレコードを抽出して投稿日時の降順で並べ替える
    queryset = NewsPost.objects.filter(
        category='economy').order_by('-posted_at')
    #1ページに表示するレコードの件数
    paginate_by = 5

class SportView(ListView):
    #sport_list.htmlをレンダリングする
    template_name = 'sport_list.html'
    #クラス変数modelにモデルNewspostを設定
    model = NewsPost
    #object_listキーの別名を設定
    context_object_name = 'sport_records'
    #category='sport'のレコードを抽出して投稿日時の降順で並べ替える
    queryset = NewsPost.objects.filter(
        category='sport').order_by('-posted_at')
    #1ページに表示するレコードの件数
    paginate_by = 5

class ContactView(FormView):
    #contact.htmlをレンダリングする
    template_name = 'contact.html'
    #クラス変数form_classにforms.pyで定義したContactFormを設定
    form_class = ContactForm
    #送信完了後にリダイレクトするメッセージ
    success_url = reverse_lazy('blogapp:contact')

    def form_valid(self, form):
        #フォームに入力されたデータをフィールド名を指定して取得
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        #メールのタイトルの書式を設定
        subject = 'お問い合わせ:{}'.format(title)
        #フォームの入力データの書式を設定
        message = \
            '送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:{3}' \
            .format(name,email,title,message)
        #メールの送信元のアドレス(outlook)
        from_email = 'utm2377081@stu.o-hara.ac.jp'
        #送信先のメールアドレス(outlook)
        to_list = ['utm2377081@stu.o-hara.ac.jp']
        #EmailMessageオブジェクトを生成
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,
                               )
        #EmailMessageクラスのsend()でメールサーバからメールを送信
        message.send()
        #送信完了後に表示するメッセージ
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        #戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)