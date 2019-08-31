<template>
  <div id="login">
    <div style="width:300px;margin:0 auto;">
      <p style="font-size:50px">重置密码</p>
      <div style="margin:10px">
        <el-input placeholder="请输入忘记密码的校园卡卡号" v-model="sno"></el-input>
      </div>
      <div style="margin:10px">
        <el-input placeholder="请输入忘记密码的校园卡学号" v-model="cno"></el-input>
      </div>
      <div style="margin:10px">
        <el-input placeholder="新密码" v-model="password1" show-password></el-input>
      </div>
      <div style="margin:10px">
        <el-input placeholder="请再次输入新密码" v-model="password2" show-password></el-input>
      </div>
      <div style="margin:10px;width:280px;">
        <el-button round style="width:100%;" @click="RPW()" type="primary">提交</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
export default {
  name: "changePassword",
  components: {},
  data() {
    return {
      sno: "",
      cno: "",
      password1: "",
      password2: "",
      count: "" //倒计时
    };
  },
  methods: {
    RPW: function() {
      // eslint-disable-next-line
      if (
        this.sno !== "" &&
        this.cno !== "" &&
        this.password1 !== "" &&
        this.password2 !== ""
      ) {
        if (this.password2 === this.password1) {
          if (this.password2.length < 8) {
            axios({
              url: "/api/RPW",
              method: "post",
              responseType: "json", // 默认的
              data: qs.stringify({
                sno: this.sno,
                cno: this.cno,
                password: this.password2
              })
            }).then(res => {
              // eslint-disable-next-line
              console.log(res);
              if (res.data.error_code == 0) {
                this.$cookie.set("login", "0", 1);
                this.$cookie.set("sno", "0", 1);
                this.$emit("func", 0);
                this.$message.success("重置密码成功！返回登录页...");
                this.clickJump(3);
              } else {
                this.$message.error("重置密码失败！请检查卡号与学号是否对应！");
              }
            });
          } else {
            this.$message.error("密码必须小于或等于八位！");
          }
        } else {
          this.$message.error("两次输入的密码不同！");
        }
      } else {
        this.$message.error("输入框不能为空！");
      }
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