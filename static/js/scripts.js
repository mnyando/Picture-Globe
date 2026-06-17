// Copy Link handler with Clipboard API and modern Toast Notification
copyLink = (elementId) => {
  const inputEl = document.getElementById(elementId);
  if (!inputEl) return;
  
  // Use modern Clipboard API if supported, fallback otherwise
  if (navigator.clipboard) {
    navigator.clipboard.writeText(inputEl.value)
      .then(() => showToast("Link copied to clipboard!"))
      .catch(err => {
        console.error("Failed to copy link using Clipboard API: ", err);
        fallbackCopy(inputEl);
      });
  } else {
    fallbackCopy(inputEl);
  }
}

function fallbackCopy(inputEl) {
  try {
    inputEl.select();
    document.execCommand("copy");
    showToast("Link copied to clipboard!");
  } catch (err) {
    console.error("Fallback copy failed: ", err);
  }
}

// Dynamically create and show a custom Toast Notification
function showToast(message) {
  // Check if a toast is already on screen and remove it
  const existingToast = document.querySelector(".toast-notification");
  if (existingToast) {
    existingToast.remove();
  }

  // Create toast element
  const toast = document.createElement("div");
  toast.className = "toast-notification";
  
  // Add checklist icon and message text (FontAwesome checkmark)
  toast.innerHTML = `
    <i class="fa fa-check-circle toast-icon"></i>
    <span>${message}</span>
  `;
  
  // Append to body
  document.body.appendChild(toast);
  
  // Trigger animation after append
  setTimeout(() => {
    toast.classList.add("show");
  }, 10);
  
  // Dismiss after 3 seconds
  setTimeout(() => {
    toast.classList.remove("show");
    // Remove from DOM after fade animation is complete
    setTimeout(() => {
      toast.remove();
    }, 400);
  }, 3000);
}

// Smooth scrolling anchors setup
function scrollToAnchors() {
  const links = document.querySelectorAll('.scroll');
  links.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href');
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        targetElement.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}

// Initialize when DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  scrollToAnchors();
});