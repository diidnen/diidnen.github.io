# Review of Fluid Mechanics

## Chapter 3: Dynamics

The material derivative (or substantial derivative):

$$\frac{D\mathbf{u}}{Dt} = \frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla)\mathbf{u}$$
 
Consider any scalar field $\alpha(\mathbf{r},t)$ and suppose the fluid element follows a pathline $\mathbf{r}(t)$. The rate of change of $\alpha$ following the fluid element is given by:

$$\frac{D\alpha}{Dt} = \frac{\partial \alpha}{\partial t} + (\mathbf{u} \cdot \nabla)\alpha$$

(This consists of local change and convective change)

The material derivative can be written in operator form as:

$$\left(\frac{\partial}{\partial t} + \mathbf{u} \cdot \nabla\right)\alpha$$

Leibniz theorem:

$$\frac{d}{dt}\int_{} f(x,t) dx = \int_{}\left(\frac{\partial f}{\partial t} + \nabla \cdot (f \mathbf{u})\right)dx$$

consider any quantity $\alpha(\mathbf{r},t)$ a fluid domain $D$ and let $u(\mathbf{r},t)$ be its fluid velocity. Let $V$ be a subvolume of D and $S$ be its surface. and moving with the fluid D so as to always contain the same fluid particles. Then the total quantity of $\alpha$ in a volume $V$ is given by:

$$Q(t) = \int_{V} u(\mathbf{r},t) dV$$

The time rate of change of $Q(t)$ is given by:

$$\frac{dQ}{dt} = \frac{d}{dt}\int_{V} u(\mathbf{r},t) dV = \int_{V}\left(\frac{\partial u}{\partial t} + \nabla \cdot (u \mathbf{u})\right)dV$$ 

(the change following a volume comprised of the same fluid particles equals the sum of the local rate of the change of $\alpha$ and the flux of $\alpha$ through the boudary of $\mathbf{V}$)

we have RTT2:

$$\frac{D}{Dt}\int_{V} \alpha(\mathbf{r},t) dV = \int_{V}\left(\frac{\partial \alpha}{\partial t} + \nabla \cdot (\alpha \mathbf{u})\right)dV$$ 

(这里的$\nabla$是从divergence theroem来的)

we have RTT3:

$$\frac{D}{Dt}\int_{V} \alpha(\mathbf{r},t) dV = \int_{V}\left(\frac{D\alpha}{Dt} + \alpha \nabla \cdot \mathbf{u}\right)dV$$

and as the mass of the fluid element is conserved, we have:

$$\frac{D}{Dt}\int_{V} \rho(\mathbf{r},t) dV = 0$$

so we can deduce that:

$$\frac{\partial \rho}{\partial t} +  \nabla \cdot (\rho \mathbf{u}) = 0$$ 

(conservation of mass)

which is the equation of continuity.


Consider any quantity $f$ associated with a fluid of density $\rho(\mathbf{r},t)$ then for any volume $V$ we have 

$$\frac{D}{Dt}\int_{V} f(\mathbf{r},t) \rho(\mathbf{r},t) dV = \int_{V}\frac{Df}{Dt} \rho(\mathbf{r},t) dV$$ 

(RTT4)


Euler equation:
 $$\frac{D\mathbf{u}}{Dt} = \frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla)\mathbf{u} = -\frac{1}{\rho}\nabla p + \mathbf{F}$$


hydrostatic pressure:
when the flow is at rest:
$$\frac{D\mathbf{u}}{Dt} = -\frac{1}{\rho} \nabla p - g\hat{z}$$

we can get archimedes principle:

$$\mathbf{F} = \int_{S} p \mathbf{n} dS = \int_{V} \nabla p dV = - \int_{V} \rho g dV = -mg\hat{z}$$

the atmospheric pressure exerts no net force on a body

then introduce dynamic pressure, which is the deviation from the hydrostatic pressure

p=p_h+p_d

p_d=$\frac{1}{2} \rho u^2$


$$\frac{D\mathbf{u}}{Dt} = -\frac{1}{\rho} \nabla p_d$$


this means that the acceleration of a fluid element is only  due to the gradient of the dynamic pressure. that the hydrostatic pressure simply balances the weight of the water

H=p+1/2$\rho u^2$+$\rho V_e$ is constant along streamlines ,note that this does not mean that the pressure takes the same value on each streamline.

Bernoulli's law is a statement of the conservation of energy following a particle in an inviscid fluid of constant density(这里要inviscid是因为不想考虑粘性力 而且在计算的时候 F be conservative)



考虑海洋中的浪花，我们假设海洋具有��限深度，并且波浪的传播是二维的（沿着 $x$ 和 $z$ 方向），且波浪的传播是线性的。在这种情况下，波浪的控制方程为：$\nabla^2 \phi = 0$


现在我们要考虑边界条件，我们假设波浪的传播是沿着 $x$ 方向的，那么我们可以得到波浪的边界条件为：

1.along this surface the pressure in the fluid balances atmosphereic pressure
可以把 $f(z)$ 在0处 展开，这样我们就可以得到 $f(z)$ 的表达式，然后我们可以apply到z=0处，这样我们就可以得到波浪的边界条件为：

$\phi(x,z=0) = g\eta(x)$

2.a particle on the surface remains on the surface:
$z-\eta(x,t)=0 and w=\frac{\partial \eta}{\partial t} z=0$
and $\frac{\partial \phi}{\partial z} = \frac{\partial^2 \eta}{\partial t^2}$ at $z=0$

好像是一个叫做disturbance pressure的东西
pressure fluctuation due to the displacement of the surface
就是感觉是在wave运动的时候产生的力

现在来找solution we are lookig for solutions that represent waves on the surface that is we want $\eta(x,t)$ to have the form $\eta(x,t)=Ae^{i(kx-\omega t)}$ (k is the wave number and $\omega$ is the angular frequency)
