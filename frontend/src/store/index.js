import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);
const state = {//要设置的全局访问的state对象
    login: false,
    cno: 0
    //要设置的初始属性值
};
const getters = {   //实时监听state值的变化(最新状态)
    isLogin(state) {  //方法名随意,主要是来承载变化的showFooter的值
        return state.login
    },
    getCno() {  //方法名随意,主要是用来承载变化的changableNum的值
        return state.cno
    }
};
const mutations = {
    loginSuccess(state) {   //自定义改变state初始值的方法，这里面的参数除了state之外还可以再传额外的参数(变量或对象);
        state.login = true;
    },
    loginFailure(state) {  //同上
        state.login = false;
    },
    changeSno(state,sno){ //同上，这里面的参数除了state之外还传了需要增加的值sum
       state.cno=sno;
    }
};
const actions = {
    loginS(context) {  //自定义触发mutations里函数的方法，context与store 实例具有相同方法和属性
        context.commit('loginSuccess');
    },
    loginF(context) {  //同上注释
        context.commit('loginFailure');
    },
    getNewS(context,num){   //同上注释，num为要变化的形参
        context.commit('changeSno',num)
     }
};
export default new Vuex.Store({
    state,
    getters,
    mutations,
    actions
});