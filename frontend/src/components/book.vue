<template>
  <div id="user">
    <div style="width:1100px">
      <div style="width:500px;float:left;margin:20px;">
        <el-button
          plain
          @click="getExpenditureInfo"
          style="margin:10px"
          icon="el-icon-refresh"
        >刷新消费账单</el-button>
        <el-table
          :data="ExpenditureInfo"
          stripe
          style="width: 100%"
          v-loading="loading1"
          element-loading-text="拼命加载中"
          element-loading-spinner="el-icon-loading"
          element-loading-background="rgba(0, 0, 0, 0.8)"
        >
          <el-table-column prop="pk" label="消费流水号" width="180"></el-table-column>
          <el-table-column prop="ccost" label="消费金额" width="180"></el-table-column>
          <el-table-column prop="ctime" label="消费时间"></el-table-column>
        </el-table>
      </div>
      <div style="width:500px;float:left;margin:20px;">
        <el-button plain @click="getIncomeInfo" style="margin:10px" icon="el-icon-refresh">刷新充值账单</el-button>
        <el-table
          :data="IncomeInfo"
          stripe
          style="width: 100%"
          v-loading="loading2"
          element-loading-text="拼命加载中"
          element-loading-spinner="el-icon-loading"
          element-loading-background="rgba(0, 0, 0, 0.8)"
        >
          <el-table-column prop="pk" label="充值流水号" width="180"></el-table-column>
          <el-table-column prop="rmoney" label="充值金额" width="180"></el-table-column>
          <el-table-column prop="rtime" label="充值时间"></el-table-column>
        </el-table>
      </div>
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
      ExpenditureInfo: new Array(),
      IncomeInfo: new Array(),
      cardNum: "",
      cname: "",
      mname: "",
      loading1: true,
      loading2: true
    };
  },
  methods: {
    getExpenditureInfo: function() {
      axios({
        url: "/api/getExpenditureInfo",
        method: "post",
        responseType: "json", // 默认的
        data: qs.stringify({
          sno: this.$cookie.get("sno")
        })
      }).then(res => {
        // eslint-disable-next-line
        console.log(res);
        if (res.data.error_code == 0) {
          this.ExpenditureInfo.splice(0, this.ExpenditureInfo.length);
          for (let index in res.data.CostInfo) {
            // eslint-disable-next-line
            console.log(res.data.CostInfo[index]);
            let x = {
              ccost: 0,
              ctime: "",
              ccardno: 0,
              pk: ""
            };
            x.ccost = res.data.CostInfo[index].fields.ccost;
            x.ctime = res.data.CostInfo[index].fields.ctime;
            x.ccardno = res.data.CostInfo[index].fields.ccardno;
            x.pk = res.data.CostInfo[index].pk;
            this.ExpenditureInfo.push(x); // eslint-disable-next-line
            console.log(x);
          }
          // eslint-disable-next-line
          console.log(this.ExpenditureInfo);
          this.$message.success("刷新成功！");
          this.loading1 = false;
        } else {
          this.$message.error("刷新失败！");
        }
      });
    },
    getIncomeInfo: function() {
      axios({
        url: "/api/getIncomeInfo",
        method: "post",
        responseType: "json", // 默认的
        data: qs.stringify({
          sno: this.$cookie.get("sno")
        })
      }).then(res => {
        if (res.data.error_code == 0) {
          this.IncomeInfo.splice(0, this.IncomeInfo.length);
          // eslint-disable-next-line
          console.log(res);
          for (let index in res.data.IncomeInfos) {
            let x = {
              rmoney: 0,
              rtime: "",
              rcardno: 0,
              pk: ""
            };
            x.rmoney = res.data.IncomeInfos[index].fields.rmoney;
            x.rtime = res.data.IncomeInfos[index].fields.rtime;
            x.rcardno = res.data.IncomeInfos[index].fields.rcardno;
            x.pk = res.data.IncomeInfos[index].pk;
            this.IncomeInfo.push(x); // eslint-disable-next-line
            console.log(x);
          }
          // eslint-disable-next-line
          console.log(this.IncomeInfo);
          this.$message.success("刷新成功！");
          this.loading2 = false;
        } else {
          this.$message.error("刷新失败！");
        }
      });
    }
  }
};
</script>

<style>
</style>