
// import { createRouter, createWebHistory } from 'vue-router'

// const routes = [
//   {
//     path: '/',
//     name: 'home',
//     component: () => import('../views/AppView_.vue')
//   },
//   {
//     path: '/login',
//     name: 'login',
//     component: () => import('../views/Login.vue')
//   },
//   {
//     path: '/driver-verification',
//     name: 'driver-verification',
//     component: () => import('../views/driver-verification.vue')
//   },
  
// ]

// const router = createRouter({
//   history: createWebHistory(process.env.BASE_URL),
//   routes
// })

// // Navigation guards
// router.beforeEach((to, from, next) => {
//   document.getElementById('progress-bar').style.display = 'block';
//   next();
// });

// router.afterEach(() => {
//   document.getElementById('progress-bar').style.display = 'none';
// });

// export default router



import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/Dashborad.vue')
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
    path: '/driver-renew',
    name: 'driver-renew',
    component: () => import('../views/driver-renew.vue')
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/about.vue')
  },
  ,
  {
    path: '/instant-loan',
    name: 'instant loan',
    component: () => import('../views/instant-loan.vue')
  },
  // Catch-all route for undefined paths
  {
    path: '/:catchAll(.*)',
    name: 'not-found',
    component: () => import('../views/NotFound.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// Navigation guards
router.beforeEach((to, from, next) => {
  document.getElementById('progress-bar').style.display = 'flex';
  next();
});

router.afterEach(() => {
  document.getElementById('progress-bar').style.display = 'none';
});

export default router
