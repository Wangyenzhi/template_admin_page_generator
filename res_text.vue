<template>
  <div class="index">
    <div class="wrap-padding-ct">
      <z_page
        title="123" :query-params.sync="queryParams"
        :table-option="table_option" :data="table_list" @press="press"/>
    </div>
    <z_view_qr v-if="z_view_qr_visible" :visible.sync="z_view_qr_visible" :view-url="previewUrl"/>
    
                                <z_dialog_form
                                 v-if="change_edit_visible" :visible="change_edit_visible"
                                 width="60%" v-model="change_active_info" :filed-width="'500px'" label-width="120px"
                                 @finish="changeFinish"
                                 @update:visible="(val)=>{
                                 change_edit_visible = val
                                 changeActiveInfoReset()
                                 }"/>
                                 <!--  model_update  -->
                                 

  </div>
</template>

<script>
import Z_page from '@/components/Z/z_page';
import { zfTemplateDataDeal, zfTurnToTemplate,deepCopy } from '@/components/Z/z_funcs';
import { prepareFormData } from '@/x';
import Z_dialog_form from '@/components/Z/z_dialog_form';
import Z_view_qr from '@/components/Z/z_view_qr';
import { apiImsApiChannelintegralPageList,apiImsApiChannelintegralAddOrUpdate } from '@/generated_api';

export default {
  name: 'index',
  components: { Z_view_qr, Z_dialog_form, Z_page },
  data() {
    return {
      change_edit_visible:false,
      z_view_qr_visible:false,
      queryParams: {
        fitter: [{'prop': 'activityEndTime', 'type': 'input', 'label': '活动结束时间', 'value': '', 'data': [], 'options': {}}, {'prop': 'activityName', 'type': 'input', 'label': '活动名称', 'value': '', 'data': [], 'options': {}}, {'prop': 'activityStartTime', 'type': 'input', 'label': '活动开始时间', 'value': '', 'data': [], 'options': {}}, {'prop': 'activityStatus', 'type': 'select', 'label': '活动状态', 'value': '', 'data': [{'key': '0', 'value': '待提交审批 '}, {'key': '1', 'value': '未开始 '}, {'key': '2', 'value': '进行中 '}, {'key': '3', 'value': '已结束'}], 'options': {}}, {'prop': 'approvalStatus', 'type': 'select', 'label': '审批状态 ', 'value': '', 'data': [{'key': '0', 'value': '待审批 '}, {'key': '1', 'value': '审批中 '}, {'key': '2', 'value': '审批拒绝 '}, {'key': '3', 'value': '审批通过 '}, {'key': '4', 'value': '审批已撤销 '}, {'key': '5', 'value': '终止审批中 '}, {'key': '6', 'value': '终止审批拒绝 '}, {'key': '7', 'value': '终止审批已撤销 '}, {'key': '8', 'value': '终止审批已通过'}], 'options': {}}, {'prop': 'channelIntegral', 'type': 'input', 'label': '积分渠道:0-汇联通', 'value': '', 'data': [], 'options': {}}, {'prop': 'id', 'type': 'input', 'label': '活动编号', 'value': '', 'data': [], 'options': {}}, {'prop': 'paymentType', 'type': 'select', 'label': '积分使用条件', 'value': '', 'data': [{'key': '0', 'value': '仅积分 '}, {'key': '1', 'value': '混合支付'}], 'options': {}}, {'prop': 'updateBy', 'type': 'input', 'label': '操作人', 'value': '', 'data': [], 'options': {}}],
        pagination: {
          pageIndex: 1,
          pageSize: 10,
          total: 0,
        },
      },
      previewUrl: '',
      copyQueryParams: {},
      table_list: [{ test: '1' }],
      table_option: [{'prop': 'activityEndTime', 'type': 'str', 'label': '活动结束时间', 'value': '', 'data': [], 'options': {}}, {'prop': 'activityName', 'type': 'str', 'label': '活动名称', 'value': '', 'data': [], 'options': {}}, {'prop': 'activityStartTime', 'type': 'str', 'label': '活动开始时间', 'value': '', 'data': [], 'options': {}}, {'prop': 'activityStatus', 'type': 'dict', 'label': '活动状态', 'value': '', 'data': [], 'options': {'dict': {'0': '待提交审批 ', '1': '未开始 ', '2': '进行中 ', '3': '已结束'}}}, {'prop': 'approvalStatus', 'type': 'dict', 'label': '审批状态 ', 'value': '', 'data': [], 'options': {'dict': {'0': '待审批 ', '1': '审批中 ', '2': '审批拒绝 ', '3': '审批通过 ', '4': '审批已撤销 ', '5': '终止审批中 ', '6': '终止审批拒绝 ', '7': '终止审批已撤销 ', '8': '终止审批已通过'}}}, {'prop': 'channelIntegral', 'type': 'str', 'label': '积分渠道:0-汇联通', 'value': '', 'data': [], 'options': {}}, {'prop': 'id', 'type': 'str', 'label': '活动编号', 'value': '', 'data': [], 'options': {}}, {'prop': 'paymentType', 'type': 'dict', 'label': '积分使用条件', 'value': '', 'data': [], 'options': {'dict': {'0': '仅积分 ', '1': '混合支付'}}}, {'prop': 'updateBy', 'type': 'str', 'label': '操作人', 'value': '', 'data': [], 'options': {}}, {'prop': 'updateByTime', 'type': 'str', 'label': '操作时间', 'value': '', 'data': [], 'options': {}}],
      change_active_info: [{'prop': 'activityEndTime', 'type': 'input', 'label': '活动结束时间', 'value': '', 'data': [], 'options': {}}, {'prop': 'activityLevel', 'type': 'input', 'label': '活动级别:0-商品', 'value': '', 'data': [], 'options': {}}, {'prop': 'activityName', 'type': 'input', 'label': '活动名称', 'value': '', 'data': [], 'options': {}}, {'prop': 'activityStartTime', 'type': 'input', 'label': '活动开始时间', 'value': '', 'data': [], 'options': {}}, {'prop': 'applyScope', 'type': 'input', 'label': '适用范围:', 'value': '', 'data': [], 'options': {}}, {'prop': 'channelIntegral', 'type': 'input', 'label': '积分渠道:0-汇联通', 'value': '', 'data': [], 'options': {}}, {'prop': 'id', 'type': 'input', 'label': '活动id(修改时传)', 'value': '', 'data': [], 'options': {}}, {'prop': 'paymentType', 'type': 'select', 'label': '积分使用条件', 'value': '', 'data': [{'key': '0', 'value': '仅积分 '}, {'key': '1', 'value': '混合支付'}], 'options': {}}, {'prop': 'refUserGroupId', 'type': 'input', 'label': '所属渠道ID', 'value': '', 'data': [], 'options': {}}, {'prop': 'remark', 'type': 'input', 'label': '备注', 'value': '', 'data': [], 'options': {}}, {'prop': 'restrictionType', 'type': 'select', 'label': '使用限制', 'value': '', 'data': [{'key': '0', 'value': '限制百分比 '}, {'key': '1', 'value': '限制价格'}], 'options': {}}, {'prop': 'restrictionValue', 'type': 'price', 'label': '混合支付使用限制值', 'value': '', 'data': [], 'options': {}}],
      copy_change_active_info: [{'prop': 'activityEndTime', 'type': 'input', 'label': '活动结束时间', 'value': '', 'data': [], 'options': {}}, {'prop': 'activityLevel', 'type': 'input', 'label': '活动级别:0-商品', 'value': '', 'data': [], 'options': {}}, {'prop': 'activityName', 'type': 'input', 'label': '活动名称', 'value': '', 'data': [], 'options': {}}, {'prop': 'activityStartTime', 'type': 'input', 'label': '活动开始时间', 'value': '', 'data': [], 'options': {}}, {'prop': 'applyScope', 'type': 'input', 'label': '适用范围:', 'value': '', 'data': [], 'options': {}}, {'prop': 'channelIntegral', 'type': 'input', 'label': '积分渠道:0-汇联通', 'value': '', 'data': [], 'options': {}}, {'prop': 'id', 'type': 'input', 'label': '活动id(修改时传)', 'value': '', 'data': [], 'options': {}}, {'prop': 'paymentType', 'type': 'select', 'label': '积分使用条件', 'value': '', 'data': [{'key': '0', 'value': '仅积分 '}, {'key': '1', 'value': '混合支付'}], 'options': {}}, {'prop': 'refUserGroupId', 'type': 'input', 'label': '所属渠道ID', 'value': '', 'data': [], 'options': {}}, {'prop': 'remark', 'type': 'input', 'label': '备注', 'value': '', 'data': [], 'options': {}}, {'prop': 'restrictionType', 'type': 'select', 'label': '使用限制', 'value': '', 'data': [{'key': '0', 'value': '限制百分比 '}, {'key': '1', 'value': '限制价格'}], 'options': {}}, {'prop': 'restrictionValue', 'type': 'price', 'label': '混合支付使用限制值', 'value': '', 'data': [], 'options': {}}],
    };
  },
  async mounted() {
    await this.getDataList();
    this.copyQueryParams = deepCopy(this.queryParams);
    this.copy_change_active_info = deepCopy(this.change_active_info)
    this.tableOperationInit();
  },
  methods: {
    press(val) {
      if (val === 'add') {
        this.$router.push({ path: 'add_or_edit', query: {} });
        // this.changeActiveInfoReset()
        // this.change_edit_visible = true

      } else if (val === 'search') {
        this.getDataList();

      } else if (val === 'reset') {
        this.queryParamsReset();
      }
    },
    tableOperationInit() {
      const tp = {}
      let target_fpt_index = this.table_option.findIndex(ele => {
        return ele.type === 'op';
      });
      this.table_option[target_fpt_index].options.tableOperationList = {
        默认: [],
      };
      console.log('this.table_option[target_fpt_index]', this.table_option[target_fpt_index]);
    },
    queryParamsReset() {
      this.queryParams = deepCopy(this.copyQueryParams);
      this.getDataList();
    },
    changeActiveInfoReset(){
        this.change_active_info = deepCopy(this.copy_change_active_info)
    },
    async getDataList() {
      let temp_q = zfTemplateDataDeal(this.queryParams.fitter);
      temp_q = { ...temp_q, ...this.queryParams.pagination };
      const data = await apiImsApiChannelintegralPageList(temp_q);
      this.table_list = data.list;
      this.queryParams.pagination.total = data.total;
    },


    async changeFinish() {
      const temp_form = await prepareFormData(zfTemplateDataDeal(this.change_active_info));
      await apiImsApiChannelintegralAddOrUpdate(temp_form);
      this.$message.success('操作成功');
      await this.getDataList()
      this.change_edit_visible = false;
    },
    async details(row) {
      this.changeActiveInfoReset()
      const res = await SOMEFUNCS_DETAIL({ id: row.id });
      this.change_active_info = zfTurnToTemplate(res, this.change_active_info);
      this.change_active_info = this.change_active_info.map(ele => {
        return { ...ele, options: { ...ele.options, disabled: true } };
      });
      this.change_edit_visible = true;
      console.log(row.id);
    },
    view(row) {
      this.previewUrl = row.previewUrl;
      this.z_view_qr_visible = true;
      console.log('row', row.previewUrl);
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
