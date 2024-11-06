import Vue from 'vue';
import VueRouter from 'vue-router';
import HomePage from '@/components/HomePage.vue';
import ResumePage from '@/components/Resume.vue';
import ArticleList from '@/components/ArticleList.vue';
import BlogArticle from '@/components/BlogArticle.vue';
import ReadingList from '@/components/ReadingList.vue';
import FocusTimer from '@/components/FocusTimer.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/resume',
    name: 'Resume',
    component: ResumePage
  },
  {
    path: '/articles/:category?',
    name: 'articles',
    component: ArticleList,
    props: route => ({
      category: route.params.category || 'All'
    })
  },
  {
    path: '/articles/:category/:path',
    name: 'BlogArticle',
    component: BlogArticle
  },
  {
    path: '/readinglist',
    name: 'ReadingList',
    component: ReadingList
  },
  {
    path: '/focustimer',
    name: 'FocusTimer',
    component: FocusTimer
  } 
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
