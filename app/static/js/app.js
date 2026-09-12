document.addEventListener("DOMContentLoaded", () => {
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    /* ---------- Flash messages auto-dismiss ---------- */
    document.querySelectorAll(".flash").forEach((flash) => {
        window.setTimeout(() => {
            flash.style.opacity = "0";
            flash.style.transform = "translateY(-4px)";
            window.setTimeout(() => flash.remove(), 250);
        }, 3500);
    });

    /* ---------- Animated summary numbers ---------- */
    function formatAmount(value, mode) {
        const fixed = value.toFixed(2);
        if (mode === "plus") return "+\u20B9" + fixed;
        if (mode === "minus") return "-\u20B9" + fixed;
        // signed: python's "%.2f" keeps the minus sign for negative numbers already
        return (value >= 0 ? "+" : "") + "\u20B9" + fixed;
    }

    document.querySelectorAll("[data-value]").forEach((el) => {
        const target = parseFloat(el.dataset.value);
        const mode = el.dataset.mode || "signed";

        if (Number.isNaN(target)) return;

        if (reduceMotion) {
            el.textContent = formatAmount(target, mode);
            return;
        }

        const duration = 900;
        const start = performance.now();

        function tick(now) {
            const elapsed = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - elapsed, 3); // ease-out-cubic
            el.textContent = formatAmount(target * eased, mode);
            if (elapsed < 1) {
                requestAnimationFrame(tick);
            } else {
                el.textContent = formatAmount(target, mode);
            }
        }

        requestAnimationFrame(tick);
    });

    /* ---------- Animated category progress bars ---------- */
    document.querySelectorAll(".progress-bar").forEach((bar) => {
        // Force a reflow so the width transition actually plays.
        requestAnimationFrame(() => {
            requestAnimationFrame(() => bar.classList.add("is-filled"));
        });
    });

    /* ---------- Delete confirmation modal ---------- */
    const overlay = document.getElementById("confirmOverlay");

    if (overlay) {
        const titleEl = document.getElementById("confirmTitle");
        const messageEl = document.getElementById("confirmMessage");
        const cancelBtn = document.getElementById("confirmCancel");
        const deleteBtn = document.getElementById("confirmDelete");
        let pendingForm = null;

        function openModal(form) {
            pendingForm = form;
            titleEl.textContent = form.dataset.confirmTitle || "Delete this entry?";
            messageEl.textContent = form.dataset.confirmMessage || "This action can't be undone.";
            overlay.classList.add("is-visible");
            deleteBtn.focus();
        }

        function closeModal() {
            overlay.classList.remove("is-visible");
            pendingForm = null;
        }

        document.querySelectorAll("form.delete-form").forEach((form) => {
            form.addEventListener("submit", (event) => {
                event.preventDefault();
                openModal(form);
            });
        });

        cancelBtn.addEventListener("click", closeModal);

        overlay.addEventListener("click", (event) => {
            if (event.target === overlay) closeModal();
        });

        document.addEventListener("keydown", (event) => {
            if (event.key === "Escape" && overlay.classList.contains("is-visible")) {
                closeModal();
            }
        });

        deleteBtn.addEventListener("click", () => {
            if (pendingForm) {
                // .submit() does not re-trigger the "submit" event listener above.
                pendingForm.submit();
            }
        });
    }
});