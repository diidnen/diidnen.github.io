<template>
  <div class="reading-list">
    <h1 class="page-title">My Reading List</h1>
    
    <!-- 当前阅读 -->
    <section :class="['book-section', { 'hide': currentlyReading.length === 0 }]">
      <h2 class="section-title">currentlyReading</h2>
      <div class="book-grid">
        <div v-for="book in currentlyReading" 
             :key="book.id" 
             @click="openGoodreads(book.goodreadsUrl)"
             class="book-card">
          <div class="book-cover">
            <img :src="book.cover" :alt="book.title">
            <div class="progress-bar">
              <div class="progress" :style="{ width: book.progress + '%' }"></div>
            </div>
          </div>
          <div class="book-info">
            <h3 class="book-title">{{ book.title }}</h3>
            <p class="book-author">{{ book.author }}</p>
            <p class="book-progress">progress: {{ book.progress }}%</p>
            <p class="book-date">start date: {{ formatDate(book.startDate) }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 已完成 -->
    <section :class="['book-section', { 'hide': completed.length === 0 }]">
      <h2 class="section-title">Finished</h2>
      <div class="book-grid">
        <div v-for="book in completed" 
             :key="book.id" 
             @click="openGoodreads(book.goodreadsUrl)"
             class="book-card">
          <div class="book-cover">
            <img :src="book.cover" :alt="book.title">
            <div class="book-rating">
              <span v-for="n in 5" 
                    :key="n" 
                    :class="['star', { filled: n <= book.rating }]">
                ★
              </span>
            </div>
          </div>
          <div class="book-info">
            <h3 class="book-title">{{ book.title }}</h3>
            <p class="book-author">{{ book.author }}</p>
            <p class="book-date">Finished date: {{ formatDate(book.completionDate) }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 愿望清单 -->
    <section :class="['book-section', { 'hide': wishlist.length === 0 }]">
      <h2 class="section-title">Expected</h2>
      <div class="book-grid">
        <div  v-for="book in wishlist" 
             :key="book.id" 
             @click="openGoodreads(book.goodreadsUrl)"
             class="book-card">
          <div class="book-cover">
            <img :src="book.cover" :alt="book.title">
          </div>
          <div class="book-info">
            <h3 class="book-title">{{ book.title }}</h3>
            <p class="book-author">{{ book.author }}</p>
            <p class="book-date">Added date: {{ formatDate(book.addedDate) }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import books from '@/data/books.json'

export default {
  name: 'ReadingList',
  
  data() {
    return {
      currentlyReading: books.currentlyReading,
      completed: books.completed,
      wishlist: books.wishlist
    }
  },

  methods: {
    formatDate(dateString) {
      return new Date(dateString).toLocaleDateString('zh-CN')
    },
    openGoodreads(url) {
      window.open(url, '_blank', 'noopener,noreferrer')
    }
  }
}
</script>

<style scoped>
.reading-list {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.page-title {
  font-size: 2rem;
  margin-bottom: 2rem;
  color: var(--color-primary);
}

.section-title {
  font-size: 1.5rem;
  margin: 2rem 0 1rem;
  color: var(--color-text);
}

.book-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.book-card {
  background: var(--color-background-soft);
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.2s;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.book-card:hover {
  transform: translateY(-5px);
}

.book-cover {
  position: relative;
  padding-top: 150%;
  background: #f0f0f0;
}

.book-cover img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.progress-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: rgba(255, 255, 255, 0.3);
}

.progress {
  height: 100%;
  background: var(--color-primary);
  transition: width 0.3s ease;
}

.book-info {
  padding: 1rem;
}

.book-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0 0 0.5rem;
}

.book-author {
  color: var(--color-text-light);
  font-size: 0.9rem;
  margin: 0 0 0.5rem;
}

.book-progress,
.book-date {
  font-size: 0.8rem;
  color: var(--color-text-light);
  margin: 0.25rem 0;
}

.book-rating {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  background: rgba(0, 0, 0, 0.7);
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
}

.star {
  color: #ccc;
  font-size: 0.8rem;
}

.star.filled {
  color: #ffd700;
}

.hide {
  display: none;
}

@media (max-width: 768px) {
  .reading-list {
    padding: 1rem;
  }

  .book-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
  }
}
</style>