document.addEventListener("DOMContentLoaded", () => {
    const links = document.querySelectorAll("a");

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

    document.body.classList.add("page-enter"); // 초기 애니메이션 클래스 추가
});