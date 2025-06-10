document.addEventListener("DOMContentLoaded", () => {
    const links = document.querySelectorAll("a");
    const pageExitOverlay = document.createElement("div");
    pageExitOverlay.className = "page-exit";
    document.body.appendChild(pageExitOverlay);

    links.forEach(link => {
        link.addEventListener("click", event => {
            event.preventDefault(); // 기본 링크 동작 방지
            const href = link.getAttribute("href"); // 링크 URL 가져오기

            pageExitOverlay.style.opacity = "1"; // 어두워지는 애니메이션 트리거
            setTimeout(() => {
                window.location.href = href; // 페이지 이동
            }, 500); // 애니메이션 지속 시간과 동일하게 설정
        });
    });

    window.addEventListener("load", () => {
        document.body.classList.add("page-enter"); // 밝아지는 애니메이션 트리거
    });
});