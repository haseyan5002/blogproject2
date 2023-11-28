from django.urls import path
from . import views

#URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'blogapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    #post_news(ニュース投稿)ページのURLパターン
    #写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreateNewsView.as_view(), name='post_news'),

    #投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/',
        views.PostSuccessView.as_view(),
        name='post_done'),

    #リクエストされたURLが「news-detail/レコードのid/」の場合
    #viewsモジュールのNewsdetailを実行
    #URLパターン名は'news-detail'
    path(
        #詳細ページのURLはnews-detail/レコードのid/」
        'news-detail/<int:pk>/',
        #viewsモジュールのNewsDetailを実行
        views.NewsDetail.as_view(),
        #URLパターンの名前を'news-detail'にする
        name = 'news_detail'
        ),
    #domesticカテゴリの一覧ページのURLパターン
    path(
        #domesticカテゴリに一覧ページのURLは「domestic-list/」
        'domestic-list/',
        #viewsモジュールのDomesticViewを実行
        views.DomesticView.as_view(),
        #URLパターンの名前を'domestic_list'にする
        name = 'domestic_list'
        ),
    #intl(international)カテゴリの一覧ページのURLパターン
    path(
        #intlカテゴリに一覧ページのURLは「intl-list/」
        'intl-list/',
        #viewsモジュールのIntlViewを実行
        views.IntlView.as_view(),
        #URLパターンの名前を'intl_list'にする
        name = 'intl_list'
        ),
    #politicsカテゴリの一覧ページのURLパターン
    path(
        #politicsカテゴリに一覧ページのURLは「politics-list/」
        'politics-list/',
        #viewsモジュールのPoliticsViewを実行
        views.PoliticsView.as_view(),
        #URLパターンの名前を'politics_list'にする
        name = 'politics_list'
        ),
    #economyカテゴリの一覧ページのURLパターン
    path(
        #economyカテゴリに一覧ページのURLは「economy-list/」
        'economy-list/',
        #viewsモジュールのEconomyViewを実行
        views.EconomyView.as_view(),
        #URLパターンの名前を'economy_list'にする
        name = 'economy_list'
        ),
    #sportカテゴリの一覧ページのURLパターン
    path(
        #sportカテゴリに一覧ページのURLは「sport-list/」
        'sport-list/',
        #viewsモジュールのSportViewを実行
        views.SportView.as_view(),
        #URLパターンの名前を'sport_list'にする
        name = 'sport_list'
        ),

    #問い合わせのページのURLのパターン
    path(
        #問い合わせのページのURLのパターンは「contact/」
        'contact/',
        #viewsモジュールのContactViewを実行
        views.ContactView.as_view(),
        #URLパターンの名前を'contact'にする
        name = 'contact'
    ),
]