<template>
  <div class="home" id="form">
    <el-row>
      <el-col :span="8">
        <h2
          class="location"
          align="left"
        >Industry: {{ category }}</h2>
        <h2
          class="location"
          align="left"
        >Location: Beijing, China</h2>
        <h2
          class="location"
          align="left"
        >Founded Date: 2017</h2>
        <h2
          class="location"
          align="left"
        >Company Size: 10-20 employees</h2>
        <h2 class="location" align="left">Last Funding Type: &nbsp;&nbsp;&nbsp;Series C</h2>
      </el-col>
      <el-col :span="8">
        <el-row>
          <div>
            <el-avatar shape="square" :size="150" :src="profilePic" @error="errorHandler">
              <img src="https://cube.elemecdn.com/e/fd/0fc7d20532fdaf769a25683617711png.png" />
            </el-avatar>
          </div>
        </el-row>
        <el-row>
          <h1></h1>
        </el-row>
        <el-row align="bottom" type="flex" justify="center">
          <h1>
            CureFit
            <br />
            <div style="font-size: 15px; color: #909399;">
              CureFit is an Indian health and fitness company offering digital and offline experiences across fitness,
              nutrition, and mental well-being
            </div>
          </h1>
          <h5></h5>
        </el-row>
      </el-col>
      <el-col :span="8">
        <el-row>
          <h2 class="follower" align="left">Applicants: 20</h2>
          <hr />
        </el-row>
        <h2 class="location" align="left">Job Type: Remote / Full Time / Intern</h2>
        <el-row style="margin-top: 15px;">
          <font-awesome-icon
            :icon="['fas', 'envelope-square']"
            size="3x"
            pull="left"
            transform="right-30"
          />
          <font-awesome-icon
            :icon="['fab', 'facebook-square']"
            size="3x"
            pull="left"
            transform="right-30"
          />
          <font-awesome-icon
            :icon="['fab', 'linkedin']"
            size="3x"
            pull="left"
            transform="right-30"
          />
          <font-awesome-icon
            :icon="['fab', 'instagram-square']"
            size="3x"
            pull="left"
            transform="right-30"
          />
          <font-awesome-icon
            :icon="['fab', 'twitter-square']"
            size="3x"
            pull="left"
            transform="right-30"
          />
        </el-row>
        <el-row></el-row>
      </el-col>
    </el-row>
    <br />
    <br />
    <br />
    <el-row :gutter="50">
      <el-col span="16" :offset="4">
        <el-tabs tab-position="left">
          <el-tab-pane label="Company Life">
            <el-row :gutter="20">
              <h2 class="companyDetail">Company Description:</h2>
              <h4 class="detailText">
                CureFit is an Indian health and fitness company offering digital and offline experiences across fitness,
                nutrition, and mental well-being. With the aim to make fitness fun and easy, CureFit gives workouts a whole
                new meaning with a range of trainer-led, group workout classes. It operates gyms under Cult.Fit, healthy food
                offerings under Eat.Fit, mental wellness through Mind.Fit and diagnostic centers through Care.fit.
              </h4>
            </el-row>
            <el-row :gutter="20">
              <h2 class="companyDetail">Vision:</h2>
              <h4 class="detailText">
                by cooperating with xxx, our DAU has been constantly growing since last year. Our next step
                is to take down the US market, and lastly we aims to become the first unicorn in fitness field
              </h4>
            </el-row>
            <el-row :gutter="20">
              <h2 class="companyDetail">Company visit:</h2>
              <h4
                class="detailText"
              >We held our monthly company online visiting @ 15th! Check out the link here -></h4>
            </el-row>
            <el-row :gutter="20">
              <h2 class="companyDetail">Team meeting:</h2>
              <h4 class="detailText">
                We don't have weekly regular meeting so far, yet we check everybody's working pace by posting report on a
                weekly basis on Slack. On top of that, we also hold team building activities every Thursday night(gotta be
                your favorite part of our company)!
              </h4>
            </el-row>
            <el-row :gutter="20">
              <h2 class="companyDetail">Working environment</h2>
              <el-col align="left" style="margin-top: 10px;">
                <el-upload
                  action="https://jsonplaceholder.typicode.com/posts/"
                  list-type="picture-card"
                  :on-preview="handlePictureCardPreview"
                  :on-remove="handleRemove"
                >
                  <i class="el-icon-plus"></i>
                </el-upload>
              </el-col>
              <el-dialog :visible.sync="dialogVisible">
                <img width="100%" :src="dialogImageUrl" alt />
              </el-dialog>
            </el-row>
          </el-tab-pane>
          <el-tab-pane label="Opening Position">
            <!-- <div style="margin-bottom: 20px;">
              <el-button size="small" @click="addTab(editableTabsValue)">add tab</el-button>
            </div> -->
            <el-tabs v-model="editableTabsValue" type="card" closable @tab-remove="removeTab">
              <el-tab-pane
                v-for="(item, index) in editableTabs"
                :key="item.name"
                :label="item.title"
                :name="item.name"
              >{{item.content[0]}}
              <br>
              {{item.content[1]}}
              <br>
              {{item.content[2]}}
              <br>
              {{item.content[3]}}
              <br>
              {{item.content[4]}}
              <br>
              {{item.content[5]}}
              <br>
              {{item.content[6]}}
              </el-tab-pane>
            </el-tabs>
          </el-tab-pane>
        </el-tabs>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="12" :offset="6"></el-col>
    </el-row>
  </div>
</template>

<style>
#form {
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1 {
  margin-top: 10px;
}
h2.follower {
  margin-bottom: 15px;
  margin-left: 80px;
  font-size: 19px;
}
h2.location {
  margin-top: 15px;
  margin-left: 80px;
  font-size: 19px;
}

.text {
  font-size: 14px;
  text-align: left;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.box-card {
  width: 500px;
  align-items: center;
}
h2.companyDetail {
  text-align: left;
  margin-left: 25px;
  margin-top: 10px;
  color: #303133;
}
h4.detailText {
  text-align: left;
  margin-left: 25px;
  color: #909399;
}
</style>

<script>
export default {
  name: "coder",
  data: () => ({
    category: "Health care, Apps",
    activeName: "story",
    dynamicTags: ["标签一", "标签二", "标签三"],
    inputVisible: false,
    inputValue: "",
    detail: [
      "1. deploy and impove robustness of company's web",
      "2. lead team of 10"
    ],
    projectDetail: [
      "1. Frontend using Vue",
      "2. Tsinghua Summer project",
      "..."
    ],
    dialogImageUrl: "",
    dialogVisible: false,
    editableTabsValue: "2",
    editableTabs: [
      {
        title: "data scientist",
        name: "1",
        content: ["1. Team mission:", "2. Team size:","3. Team current stage:", "4. Qualifications:", 
        "5. What you'll do:", "6. Geeky about our team:", "7. Contact:"]
      },
      {
        title: "App developer",
        name: "2",
        content: "Tab 2 content"
      }
    ],
    tabIndex: 2
  }),

  mounted: function() {
    this.showCoders();
  },
  methods: {
    handleClose(tag) {
      this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
    },

    showInput() {
      this.inputVisible = true;
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },

    handleInputConfirm() {
      let inputValue = this.inputValue;
      if (inputValue) {
        this.dynamicTags.push(inputValue);
      }
      this.inputVisible = false;
      this.inputValue = "";
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    addTab(targetName) {
      let newTabName = ++this.tabIndex + "";
      this.editableTabs.push({
        title: "New Tab",
        name: newTabName,
        content: "New Tab content"
      });
      this.editableTabsValue = newTabName;
    },
    removeTab(targetName) {
      let tabs = this.editableTabs;
      let activeName = this.editableTabsValue;
      if (activeName === targetName) {
        tabs.forEach((tab, index) => {
          if (tab.name === targetName) {
            let nextTab = tabs[index + 1] || tabs[index - 1];
            if (nextTab) {
              activeName = nextTab.name;
            }
          }
        });
      }

      this.editableTabsValue = activeName;
      this.editableTabs = tabs.filter(tab => tab.name !== targetName);
    }
  }
};
</script>


