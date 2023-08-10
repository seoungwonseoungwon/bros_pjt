# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mysql',
#         'USER': 'root',
#         'PASSWORD': 'rkdtmddnjs123!',
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'charset': 'utf8',
#     }
# }



DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mysql 엔진 설정
        'NAME': 'bros_db', # 데이터베이스 이름
        'USER': 'dbmasteruser', # 데이터베이스 연결시 사용할 유저 이름
        'PASSWORD': 'dkEhdakfu456!', # 유저 패스워드
        'HOST': 'ls-59016015ea4ffdbcfcd3ff80f64eb90568dd220d.cmppywhms7xk.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4', # 테이블 생성 자동으로 해줄때 쓸 인코딩,, 이거안하면 밑에꺼해도 효과 엑스
            'use_unicode': True,
        },
    }
}

SECRET_KEY = 'django-insecure-d7h#e1-s@#=a*p1d6zv^8h%-^-lj4_1mjiedbq9fo11xbf*8f$'

### local mysql 연결임 

# DATABASES = { 
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', # mysql 엔진 설정
#         'NAME': 'bros_db', # 데이터베이스 이름
#         'USER': 'root', # 데이터베이스 연결시 사용할 유저 이름
#         'PASSWORD': 'rkdtmddnjs123!', # 유저 패스워드
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#             'charset': 'utf8mb4', # 테이블 생성 자동으로 해줄때 쓸 인코딩,, 이거안하면 밑에꺼해도 효과 엑스
#             'use_unicode': True,
#         },
#     }
# }