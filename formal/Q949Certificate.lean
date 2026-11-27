import Std

namespace ComparatorGap

def moment (r : Rat) : Rat := 16 * (1-r)^2 + (8/3) * r * (1-r)

theorem moment_polynomial (r : Rat) :
    3 * (moment r - 1) = 40*r^2 - 88*r + 45 := by
  simp only [moment]
  grind

theorem sample_counts :
    ([0,1] : List Nat).flatMap (fun x => [0,1].map (fun y => x+y))
      = [0,1,1,2] := by decide +kernel

theorem rational_obstruction : moment (4/5) = 16/15 ∧ 1 < moment (4/5) := by
  decide +kernel

theorem branch_thresholds :
    (1-(3/4 : Rat))^2 * 16 = 1 ∧ (1/4 : Rat) / ((3/4)*(1-3/4)) = 4/3 := by
  decide +kernel

theorem stronger_discriminant : (88 : Nat)^2 - 4*40*45 = 16*34 ∧ 34 < (6 : Nat)^2 := by
  decide +kernel

theorem lower_margin : ((4/5 : Rat) - 3/4)/4 = 1/80 := by decide +kernel
theorem catoni_upper : (3/4 : Rat)*((1-1/4)/(1-1/12)-3/4) = 9/176 := by
  decide +kernel

#print axioms moment_polynomial
#print axioms sample_counts
#print axioms rational_obstruction
#print axioms branch_thresholds
#print axioms stronger_discriminant
#print axioms lower_margin
#print axioms catoni_upper

end ComparatorGap
