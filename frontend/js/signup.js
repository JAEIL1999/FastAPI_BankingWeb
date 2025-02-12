document.getElementById("signupForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // 기본 폼 제출 방지

    let login_id = document.getElementById("login_id").value.trim();
    let password = document.getElementById("password").value.trim();
    let name = document.getElementById("name").value.trim();
    let message = document.getElementById("message");

    // 간단한 유효성 검사
    if (login_id === "" || password === "" || name === "") {
        message.textContent = "모든 필드를 입력하세요.";
        return;
    }
    if (password.length < 6) {
        message.textContent = "비밀번호는 6자 이상이어야 합니다.";
        return;
    }

    try {
        let response = await fetch("http://localhost:8000/signup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ login_id, password, name })
        });

        let result = await response.json();

        if (response.ok) {
            message.style.color = "green";
            message.textContent = "회원가입 성공! 로그인 페이지로 이동합니다.";
            alert(`${result.name}님, 회원가입이 완료되었습니다!`);
            setTimeout(() => {
                window.location.href = "index.html"; // 로그인 페이지로 이동
            }, 0);
        } else {
            message.style.color = "red";
            message.textContent = "회원가입 실패: " + result.detail;
        }
    } catch (error) {
        console.error("회원가입 요청 실패:", error);
        message.textContent = "다른 아이디를 입력해주세요";
    }
});
