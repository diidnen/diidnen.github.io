<template>
  <div class="markdown-body" v-html="renderedContent"></div>
</template>

<script>
import MarkdownIt from 'markdown-it'
import hljs from 'highlight.js';
import 'highlight.js/styles/vs2015.css';
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
            } catch (err) {
              console.warn('Highlight error:', err);
              return str; // 发生错误时返回原始代码
            }
          }
          return str; // 如果没有指定语言或语言不支持，返回原始代码
        }
      })
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
.markdown-body {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.markdown-body h1 {
  font-size: 2em;
  margin-bottom: 1em;
}

pre {
  background: #1e1e1e;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 1.5rem 0;
  overflow-x: auto;
}

code {
  font-family: 'Fira Code', 'Consolas', monospace;
  font-size: 0.9rem;
  line-height: 1.5;
}
</style>
