<template>
  <div class="articles-container">
    <div class="articles-header">
      <h1>Articles</h1>
      <div class="category-filters">
        <button 
          v-for="category in categories" 
          :key="category"
          :class="['category-btn', { active: currentCategory === category }]"
          @click="filterByCategory(category)"
        >
          {{ category }}
        </button>
      </div>
    </div>

    <div class="articles-grid">
      <router-link 
        v-for="article in filteredArticles" 
        :key="article.path"
        :to="{
          name: 'BlogArticle',
          params: {
            category: article.category.toLowerCase(),
            path: article.path
          }
        }"
        class="article-card"
      >
        <div class="article-content">
          <span class="article-category">{{ article.category }}</span>
          <h2 class="article-title">{{ article.title }}</h2>
          <p class="article-description">{{ article.description }}</p>
          <div class="article-meta">
            <span class="article-date">{{ article.date }}</span>
            <span class="article-read-time">{{ article.readTime }} min read</span>
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
import articles from '../data/articles.json'

export default {
  name: 'ArticleList',
  props: {
    category: {
      type: String,
      default: 'All'
    }
  },
  data() {
    return {
      articles,
      currentCategory: this.category,
      categories: ['All', ...new Set(articles.map(article => article.category))]
    }
  },
  watch: {
    '$route.params.category': {
      immediate: true,
      handler(newCategory) {
        this.currentCategory = newCategory || 'All';
      }
    }
  },
  computed: {
    filteredArticles() {
      console.log('Filtering articles for category:', this.currentCategory);
      if (this.currentCategory === 'All') {
        return this.articles;
      }
      return this.articles.filter(article => 
        article.category === this.currentCategory
      );
    }
  },
  methods: {
    filterByCategory(category) {
      this.$router.push({
        name: 'articles',
        params: { 
          category: category === 'All' ? undefined : category 
        }
      });
    }
  }
}
</script>

<style scoped>
.articles-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.articles-header {
  margin-bottom: 2rem;
  text-align: center;
}

.articles-header h1 {
  font-size: 2.5rem;
  color: #2c3e50;
  margin-bottom: 1.5rem;
}

.category-filters {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.category-btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 25px;
  background: #f8f9fa;
  color: #495057;
  cursor: pointer;
  transition: all 0.3s ease;
}

.category-btn.active {
  background: #42b983;
  color: white;
}

.articles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
}

.article-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  text-decoration: none;
  color: inherit;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.article-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.article-content {
  padding: 1.5rem;
}

.article-category {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  background: #e9ecef;
  border-radius: 15px;
  font-size: 0.8rem;
  color: #495057;
  margin-bottom: 1rem;
}

.article-title {
  font-size: 1.25rem;
  color: #2c3e50;
  margin: 0.5rem 0;
}

.article-description {
  color: #6c757d;
  font-size: 0.9rem;
  line-height: 1.5;
  margin-bottom: 1rem;
}

.article-meta {
  display: flex;
  justify-content: space-between;
  color: #adb5bd;
  font-size: 0.8rem;
}

@media (max-width: 768px) {
  .articles-container {
    padding: 1rem;
  }
  
  .articles-grid {
    grid-template-columns: 1fr;
  }
  
  .category-filters {
    flex-wrap: wrap;
  }
}
</style>
