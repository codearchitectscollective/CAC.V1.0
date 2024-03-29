from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.projects, name="projects"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contact"),
    path('projects', views.projects, name="projects"),
    path('purchase', views.purchase, name="purchase"),
    path('timeline', views.timeline, name="timeline"),
    path('home', views.home, name="home"),
    path('arcade', views.arcade, name="arcade"),
    path('tetris', views.tetris, name="tetris"),
    path('snake', views.snake, name="snake"),
    path('colorpicker', views.colorpicker, name="colorpicker"),
    path('pong', views.pong, name="pong"),
    path('signup', views.signup, name="signup"),
    path('payment', views.payment, name="payment"),
    path('login', views.login, name="login"),
    path('blogmenu', views.blogmenu, name="blogmenu"),
    path('arcadegames', views.arcadegames, name="arcadegames"),
    path('mario', views.mario, name="mario"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('password', views.password, name='password'),
    path('passwordgenerator', views.passwordgenerator, name='passwordgenerator'),
    path('forgetpass', views.forgetpass, name='forgetpass'),
    path('verification', views.verification, name='verification'),
    path('resetpassword', views.resetpassword, name='resetpassword'),
    path('profile', views.profile, name='profile'),
    path('notepad', views.notepad, name='notepad'),
    path('myip', views.myip, name='myip'),
    path('camera', views.camera, name='camera'),
    path('internetspeedtest', views.internetspeedtest, name='internetspeedtest'),
    path('calculator', views.calculator, name='calculator'),
    path('settings', views.settings, name='settings'),
    path('tools', views.tools, name='tools'),
    path('logout', views.logout, name='logout'),
    path('blog/<int:post_id>/', views.post_detail_view, name='blog'),

]
