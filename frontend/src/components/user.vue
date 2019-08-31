<template>
  <div id="user">
    <el-button plain @click="getCardInfo" icon="el-icon-refresh">刷新个人数据</el-button>
    <el-divider content-position="left">学生信息</el-divider>
    <div style="margin-left:50px">
    <p>学号：{{cardInfo.sno}}</p>
    <p>姓名：{{studentInfo.sname}}</p>
    <p>性别：{{studentInfo.ssex}}</p>
    <p>出生日期：{{studentInfo.sage}}</p>
    <p>学院：{{cname}}学院</p>
    <p>专业：{{mname}}</p>
    <p>班级：{{studentInfo.sclass}}</p>
    </div>
    <el-divider content-position="left">校园卡信息</el-divider>
    <div style="margin-left:50px">
    <p>卡号：{{cardNum}}</p>
    <p>余额：{{cardInfo.cardmoney}}</p>
    <p>建卡日期：{{cardInfo.cardtime}}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
export default {
  name: "user",
  data() {
    return {
      cardInfo:{},
      studentInfo:{},
      cardNum:'',
      cname:'',
      mname:''
    };
  },
  methods: {
    getCardInfo: function() {
      axios({
          url: "/api/get_studentInfo",
          method: "post",
          responseType: "json", // 默认的
          data: qs.stringify({
            sno: this.$cookie.get('sno')
          })
        }).then(res => {
          // eslint-disable-next-line
          console.log(res);
          if (res.data.error_code == 0) {
            this.$message.success("刷新成功！");
            this.cardInfo = res.data.Cardinfo.fields;
            this.cardNum = res.data.Cardinfo.pk;
            this.studentInfo = res.data.Studentinfo.fields;
            this.mname = res.data.sspecial;
            this.cname = res.data.sdept;
          } else {
            this.$message.error("刷新失败！");
          }
          //eslint-disable-next-line
          // console.log(this.$cookie.get('sno'));
        })
    },
  }
};
</script>

<style>
</style>