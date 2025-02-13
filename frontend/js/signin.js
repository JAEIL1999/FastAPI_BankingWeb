document.getElementById("loginForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // 기본 폼 제출 방지

    let login_id = document.getElementById("login_id").value.trim();
    let password = document.getElementById("password").value.trim();
    let message = document.getElementById("message");

    if (login_id === "" || password === "") {
        message.textContent = "아이디와 비밀번호를 입력하세요.";
        return;
    }

    try {
        let response = await fetch("http://localhost:8000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ login_id, password })
        });

        let result = await response.json();

        if (response.ok) {
            message.style.color = "green";
            message.textContent = "로그인에 성공하였습니다.";
            localStorage.setItem("token", result.access_token); // JWT 토큰 저장
            alert(`${result.name}님, 반갑습니다`);
            window.location.href = `user.html?access_token=${result.access_token}`;
        } else {
            message.style.color = "red";
            message.textContent = "로그인 실패: " + result.detail;
        }
    } catch (error) {
        console.error("로그인 요청 실패:", error);
        message.textContent = "오류가 발생했습니다.";
    }
});