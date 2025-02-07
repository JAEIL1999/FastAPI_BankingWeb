banking-web/
│── backend/                
│   ├── app/
│   │   ├── main.py         # FastAPI 엔트리 포인트
│   │   ├── models/         # 데이터베이스 모델
│   │   ├── routers/        # API 라우터 (각 기능별 엔드포인트)
│   │   │   ├── users.py    # 회원가입, 로그인 관련 API
│   │   │   ├── account.py  # 계좌 관련 API (조회, 즐겨찾기, 이체, 거래내역)
│   │   ├── schemas/        # Pydantic 스키마 (데이터 검증)
│   │   ├── services/       # 비즈니스 로직
│   │   ├── dependencies.py # 공통 의존성 (예: DB 연결)
│   │   ├── config.py       # 환경설정 파일
│   ├── tests/              # 백엔드 테스트 코드
│   ├── .env                # 환경 변수 파일
│   ├── requirements.txt    # FastAPI 관련 패키지 목록
│   ├── Dockerfile          # Docker 컨테이너 설정 (필요 시)
│
│── frontend/               
│   ├── index.html          # 홈 화면
│   ├── signup.html         # 회원가입 화면
│   ├── login.html          # 로그인 화면
│   ├── account.html        # 계좌 조회 화면
│   ├── favorites.html      # 즐겨찾기 화면
│   ├── transfer.html       # 계좌이체 화면
│   ├── transaction.html    # 거래내역 화면
│   ├── assets/             # CSS, 이미지 등 정적 파일
│   ├── js/                 # JavaScript 파일 (AJAX, API 호출)
│   ├── styles/             # CSS 스타일 파일
│
│── docs/                   # 프로젝트 문서 (API 명세서, 기획서 등)
│── .gitignore              # Git에서 제외할 파일 목록
│── README.md               # 프로젝트 설명 파일
