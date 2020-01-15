<template>
  <div class="home">
    <el-row>
        <el-table :data="coderList" style="width: 100%" border>
          <el-table-column prop="id" label="id" min-width="100">
            <template scope="scope"> {{ scope.row.pk }} </template>
          </el-table-column>
          <el-table-column prop="username" label="username" min-width="100">
            <template scope="scope"> {{ scope.row.fields.username }} </template>
          </el-table-column>
        </el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      input: '',
      coderList: [],
    }
  },
  mounted: function() {
      this.showCoders()
  },
  methods: {
    showCoders(){
      this.$http.get('http://127.0.0.1:8000/api/show_Coders')
        .then((response) => {
            var res = JSON.parse(response.bodyText)
            console.log(res)
            if (res.error_num == 0) {
              this.coderList = res['data']
            } else {
              this.$message.error('fail to load coders')
              console.log(res['msg'])
            }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
