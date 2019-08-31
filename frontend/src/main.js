import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import router from './router'
import VueCookie from 'vue-cookie'
Vue.use(VueCookie)
Vue.config.productionTip = false
new Vue({
  el: '#app',
  render: h => h(App),
  router,
  template: '<App/>',
  components: { App }
}).$mount('#app')

/* eslint-disable*/
router.beforeEach((to, from, next) => {
  if (to.matched.some(res => {
    res.meta.isLoginPage === true
  }) && Vue.$cookie.get("login") == 1) {
    Vue.$cookie.set("login", "0", 1);
    next({ path: '/login', query: { redirect: to.fullPath } });
  }
  else if (to.matched.some(res => {
    res.meta.requireAuth;
  })) { // 验证是否需要登陆 
    if (Vue.$cookie.get("login") == 1) { // 查询本地存储信息是否已经登陆 
      to.matched.some(res => res.meta.requireAuth)
    } else {
      next({
        path: '/login', // 未登录则跳转至login页面 
        query: { redirect: to.fullPath } // 登陆成功后回到当前页面，这里传值给login页面，to.fullPath为当前点击的页面 
      });
    }
  } else {
    next();
  }
});
