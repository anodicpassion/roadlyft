
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/AppView_.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/driver-verification',
    name: 'driver-verification',
    component: () => import('../views/driver-verification.vue')
  },
  {
    path: '/*',
    name: 'redirects',
    component: () => import('../views/AppView_.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// Navigation guards
router.beforeEach((to, from, next) => {
  document.getElementById('progress-bar').style.display = 'block';
  next();
});

router.afterEach(() => {
  document.getElementById('progress-bar').style.display = 'none';
});

export default router

