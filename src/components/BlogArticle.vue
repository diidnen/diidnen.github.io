<template>
  <div class="blog-container">
    <article class="blog-article">
      <div class="article-content markdown-body" v-html="renderedContent"></div>
    </article>
  </div>
</template>

<script>
import MarkdownIt from 'markdown-it'
import mathjax3 from 'markdown-it-mathjax3'
import hljs from 'highlight.js';
import 'highlight.js/styles/github.css';
import articles from '@/data/articles.json';

const markdownFiles = require.context('@/assets/articles/', true, /\.md$/)

export default {
  name: 'BlogArticle',
  data() {
    return {
      content: '',
      md: new MarkdownIt({
        html: true,
        highlight: function (str, lang) {
          if (lang && hljs.getLanguage(lang)) {
            try {
              return hljs.highlight(str, { language: lang }).value;
            } catch (__) {
              console.log("highlight error", __);
            }
          }
          return ''; // 使用默认的转义
        },
        linkify: true,
        typographer: true
      }).use(mathjax3)
    }
  },
  
  async created() {
    try {
      const path = this.$route.params.path;
      const category = this.$route.params.category;
      
      console.log('Current route params:', {
        path,
        category,
        availableFiles: markdownFiles.keys(),
        attemptedPath: `./${category}/${path}.md`
      });
      
      const articleInfo = articles.find(article => article.path === path);
      console.log('Found article info:', articleInfo);
      
      if (!articleInfo) {
        throw new Error('Article not found');
      }

      const filePath = `./${category}/${path}.md`;
      console.log('Looking for file:', filePath);
      
      try {
        const content = markdownFiles(filePath);
        this.content = content.default || content;
        console.log('Content loaded successfully');
      } catch (e) {
        console.error('Failed to load markdown file:', e);
        throw e;
      }
    } catch (error) {
      console.error('Article loading error:', error);
      console.error('Available files:', markdownFiles.keys());
      this.content = '# 404\n文章未找到';
    }
  },
  
  computed: {
    renderedContent() {
      try {
        return this.md.render(this.content || '');
      } catch (error) {
        console.error('Markdown rendering error:', error);
        return '<h1>Error</h1><p>rendering error</p>';
      }
    }
  },
  
  watch: {
    async '$route.params.path'(newPath) {
      try {
        const category = this.$route.params.category;
        const articleInfo = articles.find(article => article.path === newPath);
        
        if (!articleInfo) {
          throw new Error('Article not found');
        }

        const article = await import(
          `../assets/articles/${category}/${newPath}.md`
        );
        this.content = article.default;
      } catch (error) {
        console.error('Failed to load article:', error);
        this.content = '# 404\n文章未找到';
      }
    }
  }
}
</script>

<style>
/* 整体容器 */
.blog-container {
  max-width: 900px;
  margin: 2rem auto;
  padding: 0 20px;
}

/* 文章卡片 */
.blog-article {
  background: #f3f3f3;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  padding: 2.5rem;
  transition: all 0.3s ease;
}

/* 文章内容样式 */


/* 标题样式 */





/* 代码块样式 */
.article-content pre {
  background: #f7fafc;
  border-radius: 8px;
  padding: 1.2em;
  margin: 1.5em 0;
  overflow-x: auto;
  border: 1px solid #edf2f7;
}

.article-content code {
  font-family: 'Fira Code', Consolas, Monaco, 'Andale Mono', monospace;
  font-size: 0.9em;
}

/* 行内代码样式 */
.article-content :not(pre) > code {
  background: #f7fafc;
  padding: 0.2em 0.4em;
  border-radius: 4px;
  color: #e53e3e;
  font-size: 0.9em;
}

/* 引用块样式 */
.article-content blockquote {
  margin: 1.5em 0;
  padding: 0.8em 1em;
  border-left: 4px solid #4299e1;
  background: #ebf8ff;
  border-radius: 0 4px 4px 0;
  color: #2c5282;
}

/* 列表样式 */
.article-content ul, 
.article-content ol {
  padding-left: 1.5em;
  margin: 1em 0;
}

.article-content li {
  margin: 0.5em 0;
}

/* 表格样式 */
.article-content table {
  width: 100%;
  margin: 1.5em 0;
  border-collapse: collapse;
}

.article-content th,
.article-content td {
  padding: 0.75em;
  border: 1px solid #e2e8f0;
}

.article-content th {
  background: #f7fafc;
  font-weight: 600;
}

/* 数学公式容器 */
.mjx-container {
  margin: 1.5em 0 !important;
  padding: 1em;
  background: #f8fafc;
  border-radius: 8px;
  overflow-x: auto;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .blog-container {
    padding: 0 15px;
    margin: 1rem auto;
  }

  .blog-article {
    padding: 1.5rem;
  }

  .article-content {
    font-size: 1rem;
  }

  .article-content h1 { font-size: 1.8em; }
  .article-content h2 { font-size: 1.5em; }
  .article-content h3 { font-size: 1.3em; }
}

/* 暗色模式支持 */
@media (prefers-color-scheme: dark) {
  .blog-article {
    background: #1a202c;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .article-content {
    color: #e2e8f0;
  }

  .article-content h1,
  .article-content h2,
  .article-content h3 {
    color: #f7fafc;
    border-bottom-color: #2d3748;
  }

  .article-content pre,
  .article-content :not(pre) > code {
    background: #2d3748;
    border-color: #4a5568;
  }

  .article-content blockquote {
    background: #2d3748;
    border-left-color: #4299e1;
    color: #a0aec0;
  }

  .article-content a {
    color: #63b3ed;
  }

  .article-content th,
  .article-content td {
    border-color: #4a5568;
  }

  .article-content th {
    background: #2d3748;
  }

  .mjx-container {
    background: #2d3748;
  }
}
</style>
