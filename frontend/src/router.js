import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
//组件模块
import user from './components/user'
import pay from './components/pay'
import recharge from './components/recharge'
import book from './components/book'
import changePassword from './components/changePassword'
import reportLoss from './components/reportLoss'
import registered from './components/registered'
import forgetPassword from './components/forgetPassword'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/user', name: 'user', component: user,
      meta: {
        isLoginPage: false,
        requireAuth: true, // 配置此条，进入页面前判断是否需要登陆 
      },
    },
    {
      path: '/', redirect: 'user',
      meta: {
        isLoginPage: false,
        requireAuth: true // 配置此条，进入页面前判断是否需要登陆 
      },
    },
    {
      path: '/Login', component: Login,
      meta: {
        isLoginPage: true,
        requireAuth: false // 配置此条，进入页面前判断是否需要登陆 
      },
    },
    {
      path: '/pay', component: pay,
      meta: {
        isLoginPage: false,
        requireAuth: true // 配置此条，进入页面前判断是否需要登陆 
      },
    },
    {
      path: '/recharge', component: recharge,
      meta: {
        isLoginPage: false,
        requireAuth: true // 配置此条，进入页面前判断是否需要登陆 
      },
    },
    {
      path: '/book', component: book,
      meta: {
        isLoginPage: false,
        requireAuth: true // 配置此条，进入页面前判断是否需要登陆 
      },
    },
    {
      path: '/changePassword', component: changePassword,
      meta: {
        isLoginPage: false,
        requireAuth: true // 配置此条，进入页面前判断是否需要登陆 
      },
    },
    {
      path: '/reportLoss', component: reportLoss,
      meta: {
        isLoginPage: false,
        requireAuth: true // 配置此条，进入页面前判断是否需要登陆 
      },
    },
    {
      path: '/registered', component: registered,
      meta: {
        isLoginPage: false,
        requireAuth: false // 配置此条，进入页面前判断是否需要登陆 
      },
    },
    {
      path: '/forgetPassword', component: forgetPassword,
      meta: {
        isLoginPage: false,
        requireAuth: false // 配置此条，进入页面前判断是否需要登陆 
      },
    },
  ]
})