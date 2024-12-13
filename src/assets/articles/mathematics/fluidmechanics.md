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

