// router.js - 페이지 이동 관리
function navigateTo(page) {
  const routes = {
    홈: "index.html",
    회원가입: "signup.html",
    로그인: "signin.html",
    계좌조회: "account.html",
    계좌이체: "transfer.html",
    즐겨찾기: "favorites.html",
    거래내역: "transaction.html",
  };

  if (routes[page]) {
    window.location.href = routes[page];
  } else {
    console.error("잘못된 페이지 요청:", page);
  }
}
