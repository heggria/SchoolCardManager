<template>
  <div id="app">
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
    >
      <el-menu-item id="1" index="1">{{text1}}</el-menu-item>
      <el-submenu id="2" index="2" :disabled="menuState == 0">
        <template slot="title">交易</template>
        <el-menu-item index="2-1">消费</el-menu-item>
        <el-menu-item index="2-2">充值</el-menu-item>
      </el-submenu>
      <el-menu-item id="3" index="3" :disabled="menuState == 0">账本</el-menu-item>
      <el-submenu id="4" index="4" :disabled="menuState == 0">
        <template slot="title">安全中心</template>
        <el-menu-item index="4-1">更改密码</el-menu-item>
        <el-menu-item index="4-2">紧急挂失</el-menu-item>
      </el-submenu>
      <el-menu-item id="5" index="5" :disabled="menuState == 0">退出</el-menu-item>
    </el-menu>
    <router-view @func="getLoginState" />
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      text1: "登录",
      menuState: this.$cookie.get("login")
    };
  },
  methods: {
    handleSelect: function(key) {
      // eslint-disable-next-line
      console.log(key);
      switch (key) {
        case "1":
          if (this.$cookie.get("login") == 1) this.$router.push("./user");
          else this.$router.push("./login");
          break;
        case "2-1":
          this.$router.push("./pay");
          break;
        case "2-2":
          this.$router.push("./recharge");
          break;
        case "3":
          this.$router.push("./book");
          break;
        case "4-1":
          this.$router.push("./changePassword");
          break;
        case "4-2":
          this.$router.push("./reportLoss");
          break;
        case "5":
          this.$message("已退出登录！");
          this.$cookie.set("login", "0", 1);
          this.menuState = 0;
          this.text1 = "登录";
          this.$router.push("./login");
          break;
      }
    },
    getLoginState: function(login) {
      if (login == 1) {
        this.menuState = 1;
        this.text1 = "个人中心";
      }
    }
  }
};
</script>

<style>
.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
  margin: 0;
  padding: 0;
}
.el-aside {
  background-color: rgb(145, 168, 199);
  color: #333;
  text-align: center;
  line-height: 60px;
  margin: 0;
  padding: 0;
}
#app {
  margin: 0;
  padding: 0;
}
body {
  margin: 0;
  padding: 0;
}
</style>
