document.addEventListener("DOMContentLoaded", () => {
    const links = document.querySelectorAll("a");
    const loadingScreen = document.createElement("div");
    loadingScreen.className = "loading-screen";
    loadingScreen.innerHTML = '<div class="loading-text">Loading...</div>';
    document.body.appendChild(loadingScreen);

    // 페이지 로드 완료 후 로딩 화면 제거
    window.addEventListener("load", () => {
        setTimeout(() => {
            loadingScreen.classList.add("hidden");
            document.body.classList.add("page-enter");
        }, 500); // fadeOut 애니메이션 시간과 동일하게 설정
    });

    links.forEach(link => {
        link.addEventListener("click", event => {
            event.preventDefault(); // 기본 링크 동작 방지
            const href = link.getAttribute("href"); // 링크 URL 가져오기

            document.body.classList.add("page-transition"); // 애니메이션 클래스 추가

            setTimeout(() => {
                window.location.href = href; // 페이지 이동
            }, 500); // 애니메이션 지속 시간과 동일하게 설정
        });
    });
});