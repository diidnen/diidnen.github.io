<template>
  <div class="home-container">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="profile-content">
        <img 
          src="@/assets/totoro-jumping.gif" 
          alt="Profile" 
          class="profile-image"
        />
        <h1 class="profile-title">Hello, I'm Chuhan</h1>
        <p class="profile-description">
          A passionate <span class="highlight">Mathematics</span> and 
          <span class="highlight">Computer Science</span> enthusiast, 
          currently in my second year at UCL. I like figuring out how things work(how machine learning and computer works, how to find common structure under different math objects .etc ).
          Looking at my <a href="https://github.com/diidnen" target="_blank" class="github-link">
            <i class="fab fa-github"></i> GitHub
          </a> to learn more about me(e.g transformer,full stack project() etc).
        </p>
      </div>
    </section>

    <!-- Interest Cards -->
    <section class="interest-section">
      <div class="interest-grid">
        <router-link 
          :to="{ 
            name: 'articles', 
            params: { category: 'mathematics' }
          }" 
          class="interest-card"
        >
          <div class="pixel-image-container">
            <img src="@/assets/math-dies.gif"
                 alt="Mathematics" 
                 class="interest-image pixel-image"/>
          </div>
          <h3>Mathematics</h3>
          <p>Exploring the beauty of abstract concepts and problem-solving</p>
        </router-link>
        <router-link 
          :to="{ 
            name: 'articles', 
            params: { category: 'programming' }
          }" 
          class="interest-card"
        >
          <div class="pixel-image-container">
            <img src="https://i.pinimg.com/originals/e4/26/70/e426702edf874b181aced1e2fa5c6cde.gif" 
                 alt="Programming" 
                 class="interest-image pixel-image"/>
          </div>
          <h3>Programming</h3>
          <p>Building elegant solutions through code</p>
        </router-link>
      </div>
    </section>

  
  </div>
</template>

<style scoped>
.home-container {
  background-color: white;
  min-height: 100vh;
}

.hero-section {
  padding: 6rem 2rem;
  text-align: center;
  background: linear-gradient(to bottom, #f8fafc, white);
}

.profile-content {
  max-width: 800px;
  margin: 0 auto;
}

.profile-image {
  width: 180px;
  height: 180px;
  border-radius: 50%;
  border: 4px solid white;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.profile-title {
  font-size: 2.5rem;
  color: #1e293b;
  margin-bottom: 1rem;
}

.profile-description {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #2c3e50;
  max-width: 800px;
  margin: 1.5rem auto;
  padding: 0 1rem;
  text-align: justify;
}

.highlight {
  color: #42b883;
  font-weight: 600;
  padding: 0 0.2rem;
}

.interest-section {
  padding: 4rem 2rem;
  background-color: #f8fafc;
}

.interest-grid {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  padding: 2rem;
}

.interest-card {
  background: white;
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
  text-decoration: none; 
}

.interest-card:hover {
  transform: translateY(-5px);
}

.interest-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.interest-card h3 {
  padding: 1.5rem 1.5rem 0.5rem;
  color: #1e293b;
}

.interest-card p {
  padding: 0 1.5rem 1.5rem;
  color: #64748b;
}

.articles-section {
  padding: 4rem 2rem;
}

.section-title {
  text-align: center;
  font-size: 2rem;
  color: #1e293b;
  margin-bottom: 3rem;
}

.articles-grid {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.article-card {
  background: white;
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
}

.article-card:hover {
  transform: translateY(-5px);
}

.article-image img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.article-content {
  padding: 1.5rem;
}

.article-content h3 {
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.article-content p {
  color: #64748b;
  margin-bottom: 1rem;
}

.read-more {
  color: #0ea5e9;
  text-decoration: none;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  transition: color 0.2s ease;
}

.read-more:hover {
  color: #0284c7;
}

.github-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #24292e;
  text-decoration: none;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  transition: all 0.3s ease;
}

.github-link:hover {
  background-color: #f6f8fa;
  color: #0366d6;
}

.github-link i {
  font-size: 1.2rem;
}

@media (max-width: 768px) {
  .hero-section {
    padding: 4rem 1rem;
  }

  .profile-title {
    font-size: 2rem;
  }

  .profile-description {
    font-size: 1.1rem;
  }

  .interest-grid,
  .articles-grid {
    padding: 1rem;
  }
}
</style>
