<template>
  <div id="app">
    <div class="cursor"></div>
    <div class="app-container">
      <header class="header" :class="{ 'header-hidden': !isNavVisible }">
        <div class="header-container">
          <div class="avatar-container">
            <router-link to="/" class="avatar-link">
            </router-link>
          </div>
          <nav class="nav">
            <div class="nav-links">
              <router-link
                v-for="item in navigation"
                :key="item.name"
                :to="item.href"
                class="nav-link"
                :class="{ 'nav-link-active': $route.path === item.href }"
              >
                {{ item.name }}
              </router-link>
            </div>
          </nav>
          <div class="current-time">{{ currentTime }}</div>
        </div>
      </header>
      <main class="main-content">
        <router-view></router-view>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isNavVisible: true,
      lastScrollY: 0,
      currentTime: '',
      timer: null,
      navigation: [
        { name: "About", href: "/" },
        { name: "Articles", href: "/articles" },
        { name: "Resume", href: "/resume" },
        { name: "ReadingList", href: "/readinglist" },
        { name: "Focustimer", href: "/focustimer" }
      ]
    }
  },

  mounted() {
    window.addEventListener('scroll', this.handleScroll, { passive: true })
    this.updateTime()
    this.timer = setInterval(this.updateTime, 1000)
    document.addEventListener('mousemove', this.moveCursor)
  },
  
  destroyed() {
    window.removeEventListener('scroll', this.handleScroll)
    if (this.timer) {
      clearInterval(this.timer)
    }
    document.removeEventListener('mousemove', this.moveCursor)
  },
  
  methods: {
    handleScroll() {
      const currentScrollY = window.scrollY
      this.isNavVisible = currentScrollY < this.lastScrollY || currentScrollY < 50
      this.lastScrollY = currentScrollY
    },

    updateTime() {
      const now = new Date()
      this.currentTime = now.toLocaleTimeString('en-US', {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      })
    },

    moveCursor(e) {
      const cursor = document.querySelector('.cursor')
      if (cursor) {
        cursor.style.left = e.clientX + 'px'
        cursor.style.top = e.clientY + 'px'
      }
    }
  }
}
</script>

<style>
.app-container {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

.header {
  position: fixed;
  top: 0;
  z-index: 50;
  width: 100%;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  left: 55%;
  transform: translateX(-50%);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  transition: transform 0.3s ease;
}

.header-hidden {
  transform: translate(-50%, -100%);
}

.header-container {
  display: flex;
  height: 4rem;
  max-width: 1200px;
  margin: 0 auto;
  align-items: center;
  padding: 0 1rem;
  justify-content: space-between;
}

.avatar-container {
  flex-shrink: 0;
  margin-right: 1rem;
}

.avatar-link {
  display: block;
  transition: opacity 0.2s ease-in-out;
}

.avatar-link:hover {
  opacity: 0.8;
}

.avatar {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid rgba(255, 255, 255, 0.1);
}

.nav {
  flex: 1;
  display: flex;
  justify-content: center;
}

.nav-links {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 0.5rem;
  padding: 0.25rem;
  font-size: 0.9375rem;
  font-weight: 600;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
}

.nav-link {
  display: flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
  border-radius: 0.375rem;
  padding: 0.5rem 1.25rem;
  color: rgba(0, 0, 0, 0.8);
  transition: all 0.2s ease-in-out;
}

.nav-link:hover:not(.nav-link-active) {
  color: var(--color-primary);
  background-color: rgba(255, 255, 255, 0.1);
}

.nav-link:focus-visible {
  outline: none;
  box-shadow: 0 0 0 2px var(--color-primary);
}

.nav-link-active {
  background-color: var(--color-primary);
  color: rgb(0, 0, 0);
  font-weight: 700;
}

.nav-link-active:hover {
  background-color: var(--color-primary);
  color: var(--color-background);
}

.main-content {
  margin-top: 4rem;
  flex: 1;
  padding: 1rem;
}

.current-time {
  font-size: 0.9rem;
  color: var(--color-primary);
  background: rgba(255, 255, 255, 0.1);
  padding: 0.5rem 1rem;
  border-radius: 20px;
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  font-weight: 500;
  margin-left: 1rem;
  min-width: 100px;
  text-align: center;
}

@media (max-width: 640px) {
  .nav-links {
    width: 100%;
    overflow-x: auto;
    justify-content: flex-start;
    padding: 0.25rem 0.5rem;
  }

  .nav-link {
    flex: 0 0 auto;
    font-size: 0.875rem;
    padding: 0.5rem 0.75rem;
  }

  .avatar {
    width: 2rem;
    height: 2rem;
  }
  
  .avatar-container {
    margin-right: 0.5rem;
  }

  .current-time {
    font-size: 0.8rem;
    padding: 0.3rem 0.8rem;
    margin-left: 0.5rem;
    min-width: 80px;
  }
}

/* 隐藏原始鼠标 */
* {
  cursor: none !important;
}

/* 自定义鼠标样式 */
.cursor {
  width: 8px;
  height: 8px;
  background-color: #000000;  /* 点的颜色，可以修改 */
  border-radius: 50%;
  position: fixed;
  pointer-events: none;
  z-index: 9999;

}

</style>