<template>
  <div id="login">
    <p style="font-size:50px">注册校园卡</p>
    <div style="width:300px;margin:0 auto;">
      <div style="margin:20px">
        <el-input placeholder="请输入未注册校园卡的学号" v-model="sno" clearable></el-input>
      </div>
      <div style="margin:20px">
        <el-input placeholder="请输入密码，长度不大于八位" v-model="password" show-password></el-input>
      </div>
      <div style="margin:10px">
        <el-button type="primary" round style="width:260px" @click="registered()">注册</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
export default {
  name: "registered",
  components: {},
  data() {
    return {
      sno: "",
      password: "",
      count: "" //倒计时
    };
  },
  methods: {
    registered: function() {
      // eslint-disable-next-line
      if (this.name !== "" && this.password !== "") {
        if (this.password.length <= 8) {
          axios({
            url: "/api/registered",
            method: "post",
            responseType: "json", // 默认的
            data: qs.stringify({
              sno: this.sno,
              password: this.password
            })
          }).then(res => {
            // eslint-disable-next-line
            if (res.data.error_code == 0) {
              this.$cookie.set("login", "0", 1);
              this.$cookie.set("sno", "0", 1);
              this.$emit("func", 0);
              this.$message.success("注册成功！卡号为【"+res.data.cardCode+"】30秒后自动跳转登录界面...");
              this.clickJump(300);
            } else {
              this.$message.error("注册失败！请询问管理员！");
            }
          });
        } else {
          this.$message.error("密码不能大于八位！");
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
            this.$router.push({ path: "/login" });
          }
        }, 100);
      }
    }
  }
};
</script>