import React, {Component} from 'react';
import {Card, message, Select, Table , Row , Col } from "antd";
import { Pie, G2 } from '@ant-design/plots';
import {reqPopulationData} from "../../../api";
import {SUCCESS_CODE} from "../../../config";
import "./index.less"
const { Option } = Select;


//表格配置
const columns = [
    {
        title: '年份',
        dataIndex: 'year',
        key: 'year',
    },
    {
        title: '年末总人口(万人)',
        dataIndex: 'population_num',
        key: 'population_num',
        render: value => {
            if(value===0)
                return "暂无数据"
            else
                return value
        },
    },
    {
        title: '普通本专科学生(万人)',
        key: 'student_num',
        dataIndex: 'student_num',
        render: value => {
            if(value===0)
                return "暂无数据"
            else
                return value
        },
    },
    {
        title: '在岗职工平均工资(元)',
        dataIndex: 'average_wage',
        key: 'average_wage',
        render: value => {
            if(value===0)
                return "暂无数据"
            else
                return value
        },
    },
    {
        title: '城乡居民储蓄年末余额(亿元) ',
        key: 'savings_balance',
        dataIndex: 'savings_balance',
        render: value => {
            if(value===0)
                return "暂无数据"
            else
                return value
        },
    },
];

class PopulationData extends Component {

    state = {
        data:[],
    }

    //获取数据
    getDataList = (len)=>{
        reqPopulationData(len).then((res)=>{
            const {data,code,msg}= res.data
            console.log(res.data)
            if(code===SUCCESS_CODE){
                this.setState({
                    data,
                })
            }
            else{
                message.error(msg,1)
            }
        }).catch((err)=>{
            console.log(err)
        })
    }

    componentDidMount() {
        this.getDataList(5)
    }

    render() {
        const {data} = this.state

        const chartData1 = [
            {
                type: '大专及以上',
                value: 4015258,
                percentage: 31
            },
            {
                type: '高中(含中专)',
                value: 2404391,
                percentage: 19
            },
            {
                type: '初中',
                value: 3720999,
                percentage: 28
            },
            {
                type: '小学',
                value: 1753148,
                percentage: 14
            },
            {
                type: '其他',
                value: 1059111,
                percentage: 8
            }
        ];
        const config1 = {
            height: 250,
            appendPadding: 10,
            data:chartData1,
            angleField: 'percentage',
            colorField: 'type',
            radius: 1,
            innerRadius: 0.64,
            meta: {
                value: {
                    formatter: (v) => `${v} 人`,
                },
            },
            label: {
                type: 'inner',
                offset: '-50%',
                style: {
                    textAlign: 'center',
                },
                autoRotate: false,
                content: '{value}%',
            },
            statistic: {
                title: {
                    offsetY: -4,
                    customHtml: (container, view, datum) => {
                            const text = datum ? datum.type : '常住总人口';
                            return <div style={{fontSize:'16px'}}>{text}</div>
                        },
                },
                content: {
                    offsetY: 4,
                    customHtml: (container, view, datum, data) => {
                        const text = datum ? `${datum.value} 人` : '12952907 人';
                        return <div style={{fontSize:'18px'}}>{text}</div>
                    },
                },
            },
            // 添加 中心统计文本 交互
            interactions: [
                {
                    type: 'element-selected',
                },
                {
                    type: 'element-active',
                },
                {
                    type: 'pie-statistic-active',
                },
            ],
        };

        const G = G2.getEngine('canvas');
        const chartData2 = [
            {
                sex: '男',
                sold: 51.07,
            },
            {
                sex: '女',
                sold: 48.93,
            },
        ];
        const config2 = {
            height:250,
            appendPadding: 10,
            data:chartData2,
            angleField: 'sold',
            colorField: 'sex',
            radius: 1,
            color: ['#1890ff', '#f04864'],
            label: {
                content: (obj) => {
                    const group = new G.Group({});
                    group.addShape({
                        type: 'image',
                        attrs: {
                            x: 0,
                            y: 0,
                            width: 40,
                            height: 50,
                            img:
                                obj.sex === '男'
                                    ? 'https://gw.alipayobjects.com/zos/rmsportal/oeCxrAewtedMBYOETCln.png'
                                    : 'https://gw.alipayobjects.com/zos/rmsportal/mweUsJpBWucJRixSfWVP.png',
                        },
                    });
                    group.addShape({
                        type: 'text',
                        attrs: {
                            x: 20,
                            y: 54,
                            text: obj.sex,
                            textAlign: 'center',
                            textBaseline: 'top',
                            fill: obj.sex === '男' ? '#1890ff' : '#f04864',
                        },
                    });
                    return group;
                },
            },
            tooltip: {
                fields: ['sex', 'sold'],
                formatter: (datum) => {
                    return { name: datum.sex, value: datum.sold + '%' };
                },
            },
            interactions: [
                {
                    type: 'element-active',
                },
            ],
        };

        return (
            <div>
                <Row className={"population-charts"}>
                    <Col className={"chart-small chart-left"} span={12}>
                        <div className={"chart-small-title apple-font"}>
                            学历结构
                        </div>
                        <Pie {...config1} />
                    </Col>
                    <Col className={"chart-small chart-right"} span={12}>
                        <div className={"chart-small-title apple-font"}>
                            男女比例
                        </div>
                        <Pie {...config2} />
                    </Col>
                </Row>
                <Card
                    className={"data-card"}
                    title={"人口数据"}
                    extra={
                        <Select className="data-card-select" defaultValue="5" onChange={this.getDataList}>
                            <Option value="5">最近五年</Option>
                            <Option value="10">最近十年</Option>
                            <Option value="20">最近二十年</Option>
                        </Select>
                    }
                    bodyStyle={{height:'100%',backgroundColor:'whitesmoke',padding:0,borderTop:'solid whitesmoke'}}
                >
                    <Table columns={columns} dataSource={data} pagination={false}/>
                </Card>
            </div>
        );
    }
}

export default PopulationData;
