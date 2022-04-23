import React, {Component} from 'react';
import {Card,Row,Col,Statistic} from "antd";
import { Liquid,Bullet } from '@ant-design/plots';
import "./index.less";
import BarChart from "../../../myComponents/barChart";

class DetailData extends Component {
    render() {
        const greeningRateConfig = {
            animation:true,
            height: 120,
            color: '#32CD32',
            outline: {
                border: 4,
                distance: 4,
            },
            wave: {
                length: 128,
            },
            liquidStyle: {
                fill: '#32CD32',
            }
        };
        const priceConfig = {
            data: [{
                title: '价格',
                ranges: [100000],
                reference_price: [14000],
                estimated_price: 15000,
            }],
            height: 170,
            measureField: 'reference_price',
            rangeField: 'ranges',
            targetField: 'estimated_price',
            xField: 'title',
            color: {
                range: '#f0efff',
                measure: '#5B8FF9',
                target: '#FF3333 ',
            },
            xAxis: {
                line: null,
            },
            yAxis: false,
            label: {
                measure: {
                    position: 'middle',
                    style: {
                        fill: '#fff',
                    },
                },
                target: {
                    position: 'middle',
                },
            },
            // 自定义 legend
            legend: {
                custom: true,
                position: 'bottom',
                items: [
                    {
                        value: '政府参考价',
                        name: '政府参考价',
                        marker: {
                            symbol: 'square',
                            style: {
                                fill: '#5B8FF9',
                                r: 5,
                            },
                        },
                    },
                    {
                        value: '预估价',
                        name: '预估价',
                        marker: {
                            symbol: 'line',
                            style: {
                                stroke: '#FF3333 ',
                                r: 5,
                            },
                        },
                    },
                ],
            },

        }
        return (
            <div style = {{minHeight:'100%'}}>
                <Card
                    title = {"小区名"}
                    className = {"data-card"}
                >
                    <Row gutter={[16,16]}>
                        <Col span={12}>
                            <Card>
                                <Statistic
                                    title="政府参考单价"
                                    value={11.28}
                                    precision={2}
                                    valueStyle={{ color: '#3f8600',textAlign:'center' }}
                                    suffix="元/平方米"
                                    style={{height:'60px'}}
                                />
                            </Card>
                            <Card>
                                <Statistic
                                    title="预估价"
                                    value={9.3}
                                    precision={2}
                                    valueStyle={{ color: '#cf1322',textAlign:'center' }}
                                    suffix="元/平方米"
                                    style={{height:'60px'}}
                                />
                            </Card>
                        </Col>
                        <Col span={12}>
                            <Card>
                                <Bullet {...priceConfig} />
                            </Card>
                        </Col>
                        <Col span={24}>
                            <Card>
                                <Statistic
                                    title="小区位置"
                                    value={'西安市雁塔区电子正街87号'}
                                    precision={2}
                                    valueStyle={{textAlign:'center' }}
                                />
                            </Card>
                        </Col>
                        <Col span={12}>
                            <div className={"detail-card"} style={{height:'260px'}}>
                                <h1>硬件设施</h1>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'容积率'} value={40} range={100} width={500} height={20} color={'#178dfb'}/>
                                    <h5>40</h5>
                                </div>
                                <div>
                                    <Liquid {...greeningRateConfig}  percent={0.25} />
                                    <h1 style={{textAlign:'center'}}>绿化率</h1>
                                </div>
                            </div>
                        </Col>
                        <Col span={12}>
                            <div className={"detail-card"} style={{height:'260px'}}>
                                <h1>交通配置</h1>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'公交站数量'} value={40} range={100} width={450} height={20} color={'#178dfb'}/>
                                    <h5>40</h5>
                                </div>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'地铁站数量'} value={40} range={100} width={450} height={20} color={'#178dfb'}/>
                                    <h5>40</h5>
                                </div>
                            </div>
                        </Col>
                        <Col span={12}>
                            <div className={"detail-card"} style={{height:'260px'}}>
                                <h1>教育与医疗</h1>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'幼儿园数量'} value={40} range={100} width={450} height={20} color={'#178dfb'}/>
                                    <h5>40</h5>
                                </div>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'小学数量　'} value={40} range={100} width={450} height={20} color={'#178dfb'}/>
                                    <h5>40</h5>
                                </div>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'中学数量　'} value={40} range={100} width={450} height={20} color={'#178dfb'}/>
                                    <h5>40</h5>
                                </div>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'医院数量　'} value={40} range={100} width={450} height={20} color={'#178dfb'}/>
                                    <h5>40</h5>
                                </div>
                            </div>
                        </Col>
                        <Col span={12}>
                            <div className={"detail-card"} style={{height:'260px'}}>
                                <h1>购物与休闲</h1>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'购物中心'} value={40} range={100} width={450} height={20} color={'#178dfb'}/>
                                    <h5>40</h5>
                                </div>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'超市　　'} value={40} range={100} width={450} height={20} color={'#178dfb'}/>
                                    <h5>40</h5>
                                </div>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'公园　　'} value={40} range={100} width={450} height={20} color={'#178dfb'}/>
                                    <h5>40</h5>
                                </div>
                            </div>
                        </Col>
                    </Row>
                </Card>
            </div>

        );
    }
}

export default DetailData;
