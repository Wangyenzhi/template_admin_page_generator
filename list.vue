<template>
  <div class="index">
    <div class="wrap-padding-ct">
      <p>form:{{pageData}}</p>
      <z_content v-model="pageData" :options="pageOptions"/>
    </div>
    <!--  model_update  -->
  </div>
</template>

<script>

import {deepCopy, object_set, setOptionsByKey} from "@/components/zz/z_funcs";
import { apiImsApiCommodityGroupPageList} from '@/generated_api';

export default {
  name: 'index',
  components: {},
  data() {
    return {
      change_edit_visible: false,
      z_view_qr_visible: false,
      pageData: {
        queryParams:{
          pageIndex:1,
          pageSize:5,
          total:0,
        }
      },
      pageOptions: {
        'prop': 'pageData',
        'type': 'page',
        'label': 'sadas',
        'data': [],
        'options': {},
        children:[
          {
            'prop': 'queryParams',
            'type': 'form',
            'label': '',
            'data': [],
            press:this.press,
            'options': {inline:true},
            children: [{'prop': 'adminSource', 'type': 'input', 'label': '请求来源', 'value': '', 'data': [], 'options': {}}, {'prop': 'commodityGroupSubTitle', 'type': 'input', 'label': '商品分组子标题', 'value': '', 'data': [], 'options': {}}, {'prop': 'commodityGroupTitle', 'type': 'input', 'label': '商品分组标题', 'value': '', 'data': [], 'options': {}}, {'prop': 'id', 'type': 'input', 'label': '商品分组ID', 'value': '', 'data': [], 'options': {}}, {'prop': 'reset', 'type': 'button', 'label': '重置', 'data': [], 'options': {'noFormItem': True}}, {'prop': 'search', 'type': 'button', 'label': '搜索', 'data': [], 'options': {'noFormItem': True, 'type': 'primary'}}]
          },
          {'prop': 'table_list',
            'type': 'table',
            'label': '',
            'data': [],
            'options': {loading:false,key:'table_list[0]'},
            children: [{'prop': 'commodityGroupBackgroundPic', 'type': 'img_s', 'label': '背景图', 'value': '', 'data': [], 'options': {}}, {'prop': 'commodityGroupPic', 'type': 'img_s', 'label': '商品分组图片', 'value': '', 'data': [], 'options': {}}, {'prop': 'commodityGroupSubTitle', 'type': 'str', 'label': '商品分组子标题', 'value': '', 'data': [], 'options': {}}, {'prop': 'commodityGroupTitle', 'type': 'str', 'label': '商品分组标题', 'value': '', 'data': [], 'options': {}}, {'prop': 'createBy', 'type': 'str', 'label': '创建人', 'value': '', 'data': [], 'options': {}}, {'prop': 'createTime', 'type': 'str', 'label': '创建时间', 'value': '', 'data': [], 'options': {}}, {'prop': 'groupUrl', 'type': 'str', 'label': '分组路由', 'value': '', 'data': [], 'options': {}}, {'prop': 'id', 'type': 'str', 'label': '商品分组ID', 'value': '', 'data': [], 'options': {}}, {'prop': 'remark', 'type': 'str', 'label': '备注', 'value': '', 'data': [], 'options': {}}, {'prop': 'upDownShelfStatus', 'type': 'dict', 'label': '上下架状态', 'value': '', 'data': [], 'options': {'dict': {'-2': '草稿 ', '-1': '待入库 ', '0': '待上架 ', '1': '上架 ', '2': '下架 '}}}, {'prop': 'updateBy', 'type': 'str', 'label': '操作人', 'value': '', 'data': [], 'options': {}}, {'prop': 'updateTime', 'type': 'str', 'label': '操作时间', 'value': '', 'data': [], 'options': {}}]
          },
          {
            prop: 'pageIndex', type: 'pagination', value: [1, 15, 30], data: [], options: {
              formatting: ['pageIndex', 'pageSize', 'total'],
              path:'queryParams.pageIndex'
            }, press: this.getDataList,
          },
        ]
      },
      previewUrl: '',
      copyQueryParams: {},

    };
  },
  async mounted() {
    await this.getDataList();
    this.copyQueryParams = deepCopy(this.pageData.queryParams);
    // this.copy_change_active_info = deepCopy(this.change_active_info)
    this.tableOperationInit();
  },
  methods: {
    tableOperationInit() {
      console.log('tableOperationInit')
      const tp = {}
      const tableOperationList = {
        默认: []
      };
      setOptionsByKey(this.pageOptions,'op[0]',{tableOperationList})
    },

    press(val) {
      if (val === 'add') {
        this.$router.push({path: 'add_or_edit', query: {}});
      } else if (val === 'search') {
        this.getDataList();

      } else if (val === 'reset') {
        this.queryParamsReset();
      }
    },
    async getDataList() {
      let temp_q = {}
      temp_q = {...temp_q, ...this.pageData.queryParams};
      setOptionsByKey(this.pageOptions,'table_list[0]',{loading: true})
      const data = await apiImsApiCommodityGroupPageList(temp_q).catch(()=>{
        setOptionsByKey(this.pageOptions,'table_list[0]',{loading: false})
      })
      this.pageData = object_set(this.pageData,'table_list',data.list)
      // this.pageData.pageData.table_list = data.list;
      this.pageData.queryParams.total = data.total;
      setOptionsByKey(this.pageOptions,'table_list[0]',{loading: false})

      console.log('pageData',this.pageData)
    },
    queryParamsReset() {
      this.pageData.queryParams = deepCopy(this.copyQueryParams);
      this.getDataList();
    },
    changeActiveInfoReset() {
      this.change_active_info = deepCopy(this.copy_change_active_info)
    },

    async changeFinish() {
      // const temp_form = await prepareFormData(zfTemplateDataDeal(this.change_active_info));
      // await apiImsApiCommodityGroupAdd(temp_form);
      // this.$message.success('操作成功');
      // await this.getDataList()
      // this.change_edit_visible = false;
    },

    // 函数填充

  },
};
</script>

<style lang="scss" scoped>
.index {
  padding: 20px;
  background-color: rgb(240, 242, 245);
  position: relative;
  height: calc(100vh - 100px);
  overflow: auto;

  .wrap-padding-ct {
    position: relative;
    min-height: calc(100vh - 140px);
    background-color: #ffffff;
    padding: 20px;
  }
}
</style>
