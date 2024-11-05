<template>
  <div class="resume-container">
    <!-- 顶部个人信息区 -->
    <section class="hero-section">
      <div class="profile-info">
        <h1>Chuhan Song</h1>
        <p class="tagline">Mathematics Student & Developer</p>
        <div class="contact-links">
          <a href="mailto:morrie3066924122@gmail.com" class="contact-item">
            <i class="bi bi-envelope"></i>
            <span>morrie3066924122@gmail.com</span>
          </a>
       
        </div>
      </div>
    </section>

    <!-- 技能展示区 -->
    <section class="skills-section">
      <h2>Technical Skills</h2>
      <div class="skills-grid">
        <div v-for="skill in skills" :key="skill.name" 
             class="skill-card"
             :style="{ '--skill-color': skill.color }">
          <div class="skill-header">
            <span class="skill-name">{{ skill.name }}</span>
            <span class="skill-level">{{ skill.percent }}</span>
          </div>
          <div class="skill-bar">
            <div class="skill-progress" :style="{ width: skill.percent }"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 工作经验区 -->
    <section class="experience-section">
      <h2>Experience</h2>
      <div class="timeline">
        <div v-for="(exp, index) in experiences" :key="index" class="timeline-item">
          <div class="timeline-content">
            <div class="exp-header">
              <h3>{{ exp.title }}</h3>
              <a :href="exp.link" target="_blank" class="company-name">{{ exp.company }}</a>
              <span class="date">{{ exp.dateRange }}</span>
            </div>
            <p class="description">{{ exp.description }}</p>
            <ul class="achievements">
              <li v-for="(point, pIndex) in exp.points" :key="pIndex">{{ point }}</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- 教育背景区 -->
    <section class="education-section">
      <h2>Education</h2>
      <div class="education-card">
        <h3>University College London</h3>
        <p class="degree">B.S. Mathematics</p>
        <p class="year">2023 - 2026</p>
      </div>
    </section>
  </div>
</template>

<script>
import skills from '../data/skills.json'
import experiences from '../data/experience.json'

export default {
  name: "ResumePage",
  data() {
    return {
      skills,
      experiences
    }
  }
}
</script>

<style scoped>
.resume-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  background: #ffffff;
}

.hero-section {
  text-align: center;
  padding: 4rem 2rem;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  border-radius: 20px;
  margin-bottom: 3rem;
}

.profile-info h1 {
  font-size: 3rem;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.tagline {
  font-size: 1.2rem;
  color: #6c757d;
  margin-bottom: 2rem;
}

.contact-links {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #495057;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 25px;
  background: white;
  transition: all 0.3s ease;
}

.contact-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  color: var(--color-primary);
}

.skills-section {
  margin-bottom: 3rem;
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.skill-card {
  padding: 1.5rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease;
}

.skill-card:hover {
  transform: translateY(-5px);
}

.skill-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.skill-name {
  font-weight: 500;
  color: #2c3e50;
}

.skill-level {
  color: var(--skill-color);
}

.skill-bar {
  height: 8px;
  background: #f0f0f0;
  border-radius: 4px;
  overflow: hidden;
}

.skill-progress {
  height: 100%;
  background: var(--skill-color);
  border-radius: 4px;
  transition: width 1s ease-out;
}

.timeline {
  position: relative;
  padding: 2rem 0;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  width: 2px;
  background: var(--color-primary);
}

.timeline-item {
  position: relative;
  padding-left: 2rem;
  margin-bottom: 3rem;
}

.timeline-item::before {
  content: '';
  position: absolute;
  left: -6px;
  top: 0;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--color-primary);
}

.timeline-content {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.exp-header {
  margin-bottom: 1rem;
}

.exp-header h3 {
  color: #2c3e50;
  margin: 0;
}

.company-name {
  color: var(--color-primary);
  text-decoration: none;
  font-weight: 500;
}

.date {
  display: block;
  color: #6c757d;
  font-size: 0.9rem;
  margin-top: 0.5rem;
}

.achievements {
  list-style-type: none;
  padding: 0;
}

.achievements li {
  position: relative;
  padding-left: 1.5rem;
  margin-bottom: 0.5rem;
  line-height: 1.6;
}

.achievements li::before {
  content: "→";
  color: var(--color-primary);
  position: absolute;
  left: 0;
}

.education-section {
  margin-top: 3rem;
}

.education-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  text-align: center;
}

.education-card h3 {
  color: #2c3e50;
  margin: 0;
}

.degree {
  color: var(--color-primary);
  font-weight: 500;
  margin: 0.5rem 0;
}

.year {
  color: #6c757d;
}

@media (max-width: 768px) {
  .resume-container {
    padding: 1rem;
  }

  .hero-section {
    padding: 2rem 1rem;
  }

  .profile-info h1 {
    font-size: 2rem;
  }

  .contact-links {
    flex-direction: column;
    align-items: center;
  }

  .timeline::before {
    left: 15px;
  }

  .timeline-item {
    padding-left: 2.5rem;
  }
}
</style>
