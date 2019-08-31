<template>
  <div id="login">
    <img src="@/assets/logo.png" />
    <p style="font-size:50px">学生校园卡管理系统</p>
    <div style="width:300px;margin:0 auto;">
      <div style="margin:20px">
        <el-input placeholder="学号" v-model="name" clearable></el-input>
      </div>
      <div style="margin:20px">
        <el-input placeholder="密码" v-model="password" show-password></el-input>
      </div>
      <div style="margin:10px">
        <el-button type="primary" round style="width:260px" @click="login()">登录</el-button>
      </div>
      <div style="margin:10px">
        <el-button round style="width:125px;" @click="goToRegistered()">注册</el-button>
        <el-button round style="width:125px;" @click="goToForgetPassword()">忘记密码</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
export default {
  name: "login",
  components: {},
  data() {
    return {
      sno: 0,
      name: "",
      password: "",
      apiUrl: "/api/show_studentInfo",
      collegeInfoList: [],
      majorInfoList: [],
      classInfoList: [],
      studentInfoList: [],
      count: "" //倒计时
    };
  },
  methods: {
    getCollegeInfo: function() {
      axios.get(this.apiUrl).then(response => {
        if (response.data.error_num === 0) {
          this.collegeInfoList = response.data.list;
          // eslint-disable-next-line
          console.log(this.collegeInfoList);
        } else {
          // eslint-disable-next-line
          console.log("Get info error!");
        }
      });
    },
    getMajorInfo: function() {
      axios.get(this.apiUrl).then(response => {
        if (response.data.error_num === 0) {
          this.majorInfoList = response.data.list;
          // eslint-disable-next-line
          console.log(this.majorInfoList);
        } else {
          // eslint-disable-next-line
          console.log("Get info error!");
        }
      });
    },
    getClassInfo: function() {
      axios.get(this.apiUrl).then(response => {
        if (response.data.error_num === 0) {
          this.classInfoList = response.data.list;
          // eslint-disable-next-line
          console.log(this.classInfoList);
        } else {
          // eslint-disable-next-line
          console.log("Get info error!");
        }
      });
    },
    getStudentInfo: function() {
      this.$router.push("./user");
      axios.get(this.apiUrl).then(response => {
        if (response.data.error_num === 0) {
          this.studentInfoList = response.data.list;
          // eslint-disable-next-line
          console.log(this.studentInfoList);
        } else {
          // eslint-disable-next-line
          console.log("Get info error!");
        }
      });
    },
    login: function() {
      // eslint-disable-next-line
      if (this.name !== "" && this.password !== "") {
        this.sno = this.name;
        axios({
          url: "/api/login",
          method: "post",
          responseType: "json", // 默认的
          data: qs.stringify({
            sno: this.sno,
            password: this.password
          })
        }).then(res => {
          // eslint-disable-next-line
          if (res.data.error_code == 0) {
            this.$cookie.set("login", "1", 1);
            this.$cookie.set("sno", this.name, 1);
            this.$emit("func", 1);
            this.$message.success("登录成功！跳转个人中心...");
            this.clickJump(3);
          } else {
            this.$message.error("学号或密码错误！");
          }
        });
      } else {
        this.$message.error("输入框不能为空！");
      }
    },
    loginSuccessful: function() {
      this.$emit("func", true);
    },
    goToRegistered: function(){
      this.$router.push({ path: "/registered" });
    },    
    goToForgetPassword: function(){
      this.$router.push({ path: "/forgetPassword" });
    },
    clickJump(timejump) {
      if (!this.timer) {
        this.count = timejump;
        this.show = false;
        this.timer = setInterval(() => {
          if (this.count > 0 && this.count <= timejump) {
            this.count--;
          } else {
            this.show = true;
            clearInterval(this.timer);
            this.timer = null;
            //跳转的页面写在此处
            this.$router.push({ path: "/user" });
          }
        }, 100);
      }
    }
  }
};
</script>

<style>
#login {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>