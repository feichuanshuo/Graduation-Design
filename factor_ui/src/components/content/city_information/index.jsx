import React, {Component} from 'react';
import {Card, message, Select, Table , Row , Col } from "antd";
import { Pie, G2,Line , DualAxes ,Column} from '@ant-design/plots';
import {reqCityInformation} from "../../../api";
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

class CityInformation extends Component {

    state = {
        data:[],
    }

    //获取数据
    getDataList = (len)=>{
        reqCityInformation(len).then((res)=>{
            const {data,code,msg}= res
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


        let chartData3 = []
        data.map((item)=>{
            let newRow = {
                name:'年末总人口',
                num : item.population_num === 0 ? '暂无' : item.population_num,
                year: item.year
            }
            chartData3.push(newRow)
            newRow = {
                name: '普通本专科学生',
                num : item.student_num ===0 ? '暂无' : item.student_num,
                year: item.year
            }
            chartData3.push(newRow)
        })
        chartData3.reverse()
        const config3 = {
            height:250,
            appendPadding: 10,
            data: chartData3,
            xField: 'year',
            yField: 'num',
            seriesField: 'name',
            yAxis: {
                label: {
                    formatter: (v) => `${v} 万人`,
                },
            },
            legend: {
                position: 'top',
            },
            smooth: true,
            // @TODO 后续会换一种动画方式
            animation: {
                appear: {
                    animation: 'path-in',
                    duration: 5000,
                },
            },
        };

        const chartData4 = [...data].reverse()
        const config4 = {
            height:250,
            appendPadding: 10,
            data: [chartData4, chartData4],
            xField: 'year',
            yField: ['average_wage', 'savings_balance'],
            meta: {
                average_wage: {
                    alias: '在岗职工平均工资(元)',
                },
                savings_balance: {
                    alias: '城乡居民储蓄年末余额(亿元)',
                },
            },
            geometryOptions: [
                {
                    geometry: 'line',
                    color: '#5B8FF9',
                    point: {
                        size: 5,
                        shape: 'circle',
                        style: {
                            fill: 'white',
                            stroke: '#5B8FF9',
                            lineWidth: 2,
                        },
                    },
                },
                {
                    geometry: 'line',
                    color: '#29cae4',
                    point: {
                        size: 5,
                        shape: 'diamond',
                        style: {
                            fill: 'white',
                            stroke: '#29cae4',
                            lineWidth: 2,
                        },
                    },
                },
            ],
            xAxis: {
                label: {
                    autoRotate: true,
                    autoHide: false,
                    autoEllipsis: false,
                },
            },
            yAxis: {
                area: {
                    label: {
                        formatter: (v) => {
                            return `${v}`;
                        },
                    },
                },
                price: {
                    label: {
                        formatter: (v) => {
                            return `${v}`;
                        },
                    },

                },
            },
            legend: {
                itemName: {
                    formatter: (text, item) => {
                        return item.value === 'average_wage' ? '在岗职工平均工资(元)' : '城乡居民储蓄年末余额(亿元)';
                    },
                },
            },
        };

        const chartData5 = [...data].reverse()
        const config5 = {
            height:250,
            appendPadding: 10,
            data: [chartData5, chartData5],
            xField: 'year',
            yField: ['hospital_num', 'doctor_num'],
            meta: {
                hospital_num: {
                    alias: '医院数(个)',
                },
                doctor_num: {
                    alias: '执业(助理)医师数(万人)',
                },
            },
            geometryOptions: [
                {
                    geometry: 'column',
                    color: '#5B8FF9',
                },
                {
                    geometry: 'line',
                    color: '#5AD8A6',
                },
            ],
        };

        let chartData6 = []
        data.map((item)=>{
            let newRow = {
                type:'道路交通等效声级dB(A)',
                dB : item.traffic_noise,
                year: item.year
            }
            chartData6.push(newRow)
            newRow = {
                type: '环境噪声等效声级dB(A)',
                dB : item.ambient_noise,
                year: item.year
            }
            chartData6.push(newRow)
        })

        chartData6.reverse()
        const config6 = {
            height:250,
            appendPadding: 10,
            data: chartData6,
            xField: 'year',
            yField: 'dB',
            seriesField: 'type',
            isGroup: 'true',
            columnStyle: {
                radius: [20, 20, 0, 0],
            },
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
                <Row className={"population-charts"}>
                    <Col className={"chart-small chart-left"} span={12}>
                        <div className={"chart-small-title apple-font"}>
                            人口年数据
                        </div>
                        <Line {...config3} />
                    </Col>
                    <Col className={"chart-small chart-right"} span={12}>
                        <div className={"chart-small-title apple-font"}>
                            收入情况
                        </div>
                        <DualAxes {...config4} />
                    </Col>
                </Row>
                <Row className={"population-charts"}>
                    <Col className={"chart-small chart-left"} span={12}>
                        <div className={"chart-small-title apple-font"}>
                            医疗数据
                        </div>
                        <DualAxes {...config5} />
                    </Col>
                    <Col className={"chart-small chart-right"} span={12}>
                        <div className={"chart-small-title apple-font"}>
                            噪音情况
                        </div>
                        <Column {...config6} />
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

export default CityInformation;
