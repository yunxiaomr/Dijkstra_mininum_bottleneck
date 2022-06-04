# Dijkstra_mininum_bottleneck

## 1.Question：
In lecture we define the length of a path to be the sum of the lengths of its edges. Define the bottleneck of a path to be the maximum length of one of its edges. A mininum-bottleneck path between two vertices s and t is a path with bottleneck no larger than that of any other s−t path. Show how to modify Dijkstra’s algorithm to compute a minimum-bottleneck path between two given vertices. The running time should be 𝑂(𝑚log𝑛), as in lecture.

本题为来自斯坦福算法课的一道算法题，同时也为山西大学计算机与信息技术学院 研究生算法课中抛出的进阶算法题。

## 2.Definition：
 - 2.1 路径的长度为一条路径各边长度之和；
 - 2.2 路径的bottleneck为一条路径的各边中边的最大的length；
 - 2.3 S-T两个之间的mininum-bottleneck路径为S-T之间带有最小bottleneck的路径的长度；
 - 2.4 要求：O(mlogn)
 
## 3.Solution：
#### 3.1 时间复杂度的限制；
Dijkstra：O(mn)---> O(n^2) --->O(mlogn)(引入堆排)，因此本题要想保证O(mlogn)的复杂度，除了对边进行遍历外，还需要引入小顶堆。

#### 3.2 bottleneck的限制；
路径的bottleneck为一条路径的各边中边的最大的length；在进行迭代的过程中，需要将保留这个最大值的信息。

#### 3.3 mini_bottleneck的限制；
S-T两个之间的mininum-bottleneck路径为S-T之间带有最小bottleneck的路径的长度；在得到最大值信息外，下一次进行保留的信息就是在当前保留的最大值中进行选取最小值。

综上，引入公式：
∀𝑢∈𝑋,𝑣∈𝑉−𝑋，𝑑𝑖𝑠𝑡(𝑣)=min(𝑑𝑖𝑠𝑡(𝑣),max(𝑑𝑖𝑠𝑡(𝑢),𝑤𝑒𝑖𝑔ℎ𝑡(𝑢,𝑣)))

#### 3.4 Dijkstra：
∀𝑢∈𝑋,𝑣∈𝑉−𝑋，𝑑𝑖𝑠(𝑣)=min(𝑑𝑖𝑠𝑡(𝑣),𝑑𝑖𝑠𝑡(𝑢)+𝑤𝑒𝑖𝑔ℎ𝑡(𝑢,𝑣))

#### 3.5 Dijkstra_mininum_bottleneck：
∀𝑢∈𝑋,𝑣∈𝑉−𝑋，𝑑𝑖𝑠𝑡(𝑣)=min(𝑑𝑖𝑠𝑡(𝑣),max(𝑑𝑖𝑠𝑡(𝑢),𝑤𝑒𝑖𝑔ℎ𝑡(𝑢,𝑣)))
 - 3.5.1 bottleneck = max(𝑑𝑖𝑠𝑡(𝑢),𝑤𝑒𝑖𝑔ℎ𝑡(𝑢,𝑣))
	保证先取到bottleneck；拿到的是路长值；
 - 3.5.2 min(𝑑𝑖𝑠𝑡(𝑣), bottleneck)
  保证拿到的值为bottleneck中的最小值，即为mininum_bottleneck;此时𝑑𝑖𝑠𝑡(𝑣)记录的是当前两节点之间的bottleneck值，然后通过不断的迭代，最终走到目标节点。
  
## 4.Data Example：
6 7   
1 2 3   
2 3 2   
1 3 30   
3 4 20   
4 5 30   
3 5 6   
5 6 1   

## Conference 
https://blog.csdn.net/weixin_41297324/article/details/111506679  
https://github.com/LSijing/Algorithms-Stanford   
https://blog.asarkar.com/algorithms-design-analysis/hw-5-opt/   
https://github.com/aleksandrpak/solutions/tree/master/coursera/algorithms_design_and_analysis_part_1   
